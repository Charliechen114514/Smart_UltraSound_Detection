import time
import numpy as np
import torch
import torch.nn as nn
import torchvision.transforms as transforms
from sklearn.model_selection import train_test_split
from torch.utils.data import DataLoader, Dataset
from model_train.ModelUsing import Classifier
import cv2
import os
from loguru import logger
from Core.Common.path_utils import PathUtils

# 定义自己的数据集
class ImgDataset(Dataset):
    def __init__(self, x, y=None, transform=None):
        self.x = x
        # label is required to be a LongTensor
        self.y = y
        if y is not None:
            self.y = torch.LongTensor(y)
        self.transform = transform

    def __len__(self):
        return len(self.x)

    def __getitem__(self, index):
        X = self.x[index]
        if self.transform is not None:
            X = self.transform(X)
        if self.y is not None:
            Y = self.y[index]
            return X, Y
        else:  # 如果没有标签那么只返回X
            return X


lists = []
labels = []
imgs = []

if not PathUtils.check_paths_if_exsit("model_train/model_sources"):
    logger.error("Sorry! the data using for train is private :(")
    logger.error("But you can use by using your owns with images and datas")
    exit(-1)

for picPath in os.listdir("model_train/model_sources/normal"):
    lists.append("model_train/model_sources/normal/" + picPath)

for picPath in os.listdir("model_train/model_sources/outlier"):
    lists.append("model_train/model_sources/outlier/" + picPath)

for cur in open("model_train/model_sources/labels.txt"):
    labels.append(int(cur[0]))

for cur in open("model_train/model_sources/labels2.txt"):
    labels.append(int(cur[0]))

for path in lists:
    tmp = cv2.imread(path)
    # tmp = cv2.cvtColor(tmp, cv2.COLOR_BGR2GRAY)  # 先要转换为灰度图片
    imgs.append(cv2.resize(tmp, (256, 256)))

train_transform = transforms.Compose([
    transforms.ToPILImage(),
    transforms.RandomHorizontalFlip(),  # 随机将图片水平翻转
    transforms.ToTensor()  # 将图片转成 Tensor, 并把数值normalize到[0,1](data normalization)
])

# testing 时不需做 data augmentation
test_transform = transforms.Compose([
    transforms.ToPILImage(),
    transforms.ToTensor()
])

logger.info(f"now we counted {len(lists)} images with label {len(labels)}")

imgs = np.array(imgs)
labels = np.array(labels)

train_imgs, test_imgs, train_labels, test_labels = train_test_split(imgs, labels, test_size=0.2, shuffle=True)
train_train_imgs, train_val_imgs, train_train_labels, train_val_labels = train_test_split(train_imgs, train_labels,
                                                                                          test_size=0.24, shuffle=True)

BATCH_SIZE = 12
train_set = ImgDataset(train_train_imgs, train_train_labels, train_transform)
val_set = ImgDataset(train_val_imgs, train_val_labels, test_transform)
train_loader = DataLoader(train_set, batch_size=BATCH_SIZE, shuffle=True)
val_loader = DataLoader(val_set, batch_size=BATCH_SIZE, shuffle=True)
MergeTrainValEpoch = 20
Split_Train_Val_Epoch = 35

# 使用training set訓練，並使用validation set尋找好的參數
model = Classifier().cuda()
loss = nn.CrossEntropyLoss()  # 因為是 classification task，所以 loss 使用 CrossEntropyLoss
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)  # optimizer 使用 Adam

for epoch in range(Split_Train_Val_Epoch):
    epoch_start_time = time.time()
    train_acc = 0.0
    train_loss = 0.0
    val_acc = 0.0
    val_loss = 0.0

    model.train()
    for i, data in enumerate(train_loader):
        optimizer.zero_grad()  # 用 optimizer 將 model 參數的 gradient 歸零
        train_pred = model(data[0].cuda())  # 利用 model 得到預測的機率分佈 這邊實際上就是去呼叫 model 的 forward 函數
        batch_loss = loss(train_pred, data[1].cuda())  # 計算 loss （注意 prediction 跟 label 必須同時在 CPU 或是 GPU 上）
        batch_loss.backward()  # 利用 back propagation 算出每個參數的 gradient
        optimizer.step()  # 以 optimizer 用 gradient 更新參數值

        train_acc += np.sum(np.argmax(train_pred.cpu().data.numpy(), axis=1) == data[1].numpy())
        train_loss += batch_loss.item()

    logger.info('[%03d/%03d] %2.2f sec(s) Train Acc: %3.6f  Loss: %3.6f' % \
            (epoch + 1, Split_Train_Val_Epoch, time.time() - epoch_start_time, \
            train_acc / train_set.__len__(), train_loss / train_set.__len__()))
    model.eval()
    with torch.no_grad():
        for i, data in enumerate(val_loader):
            val_pred = model(data[0].cuda())
            batch_loss = loss(val_pred, data[1].cuda())

            val_acc += np.sum(np.argmax(val_pred.cpu().data.numpy(), axis=1) == data[1].numpy())
            val_loss += batch_loss.item()

        # 將結果 logger.info 出來
        logger.info('[%03d/%03d] %2.2f sec(s) Train Acc: %3.6f Loss: %3.6f | Val Acc: %3.6f loss: %3.6f' % \
              (epoch + 1, Split_Train_Val_Epoch, time.time() - epoch_start_time, \
               train_acc / train_set.__len__(), train_loss / train_set.__len__(),val_acc / val_set.__len__(),
               val_loss / val_set.__len__()))


logger.info("Training complicated")

test_set = ImgDataset(test_imgs, transform=test_transform)
test_loader = DataLoader(test_set, batch_size=BATCH_SIZE, shuffle=False)
model.eval()
prediction = []
with torch.no_grad():
    for i, data in enumerate(test_loader):
        test_pred = model(data.cuda())
        test_label = np.argmax(test_pred.cpu().data.numpy(), axis=1)
        for y in test_label:
            prediction.append(y)

prediction = np.array(prediction)


def calcAcc(prediction, real):
    acc = 0
    for i in range(len(real)):
        if real[i] == prediction[i]:
            acc = acc + 1

    return acc / len(real)


racc = calcAcc(prediction, test_labels)
# 打印相关数据看看
logger.info("预测测试数据")
logger.info(test_labels)
logger.info("实际测试标签")
logger.info(test_labels)
logger.info("准确率")
logger.info(racc)

torch.save(model, "model_train/model.pt")