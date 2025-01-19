#!/bin/bash

command=$1

case "$command" in
    # Setup the environment
    "--setup")
        echo "Setting up the necessities..."
        poetry install
        echo "Setup the necessities done"
        ;;
    
    # Open the designer
    "--open_designer")
        echo "Opening Designer..."
        poetry run python ./dev_tools/open_designer.py
        ;;
    
    # Summon the UI file
    "--summon_uipy")
        echo "Transforming the UI files..."
        echo "Transforming the MainWindow UI file..."
        poetry run python ./dev_tools/transfer_to_uipy.py ./Ui/MainWindow/MainWindow.ui
        echo "Transforming the Browse Guide UI file..."
        poetry run python ./dev_tools/transfer_to_uipy.py ./Ui/BrowsingGuide/BrowsingGuide.ui
        echo "Transforming the InfoWindow UI file..."
        poetry run python ./dev_tools/transfer_to_uipy.py ./Ui/InfoWindow/InfoWindow.ui
        echo "Transforming the ProcessingWindow UI file..."
        poetry run python ./dev_tools/transfer_to_uipy.py ./Ui/ProcessingWindow/ProcessingWindow.ui
        echo "Transforming the SelectiveWindow UI file..."
        poetry run python ./dev_tools/transfer_to_uipy.py ./Ui/SelectiveWindow/SelectiveWindow.ui
        echo "Transforming the UI files done!"
        ;;
    
    "--summon_rccpy")
        echo "Transforming the RCC files..."
        poetry run python ./dev_tools/transfer_rcc_to_py.py ./sources/icons.qrc runtimes_middlewares/rc_py/icons_rc.py
        echo "Transforming the RCC files done!"
        ;;
    
    # Run the main application
    "--run")
        echo "Running main application directly..."
        poetry run python -m smartultrasound_detection.main
        echo "Main application quit"
        ;;
    
    "--prepare")
        echo "Setting up environments for the main application..."
        poetry run python -m smartultrasound_detection.pre_main
        echo "Pre-setup done!"
        ./devtools.sh --summon_rccpy
        ./devtools.sh --summon_uipy
        echo "Setup finished!"
        ;;
    
    "--all")
        ./devtools.sh --prepare
        ./devtools.sh --run
        ;;
    
    "--clean")
        echo "Cleaning the sources..."
        poetry run python -m clean_up.clean
        echo "Clean up done"
        ;;
    
    "--train")
        echo "Starting model training..."
        poetry run python -m model_train.model_train
        echo "Model training done. Check the train folder for usage."
        ;;
    
    "--test")
        echo "Testing the main functionalities..."
        poetry run pytest
        echo "Test done"
        ;;
    
    "--help")
        echo -e "Usage: devtools.sh [OPTIONS]\n"
        echo -e "Options:"
        echo -e "\t--setup\t\t\tSetup the environment, which will install the dependencies automatically."
        echo -e "\t--open_designer\t\tOpen Designer and launch the Designer application."
        echo -e "\t--summon_uipy\t\tSummon UI from the .ui file and transform it into the UI Python code."
        echo -e "\t--run\t\t\tRun the main application directly."
        echo -e "\t--prepare\t\tSet up environments for the main application and perform necessary transformations."
        echo -e "\t--all\t\t\tSet up environments and run the main application."
        echo -e "\t--help\t\t\tShow this help message and exit."
        echo -e "\t--clean\t\t\tClean up the runtime middlewares and the pycaches."
        echo -e "\t--test\t\t\tTest the functionalities if required."
        ;;
    
    *)
        echo "Unknown command. Please use one of the following:"
        ./devtools.sh --help
        ;;
esac
