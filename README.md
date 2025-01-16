# Smart UltraSound Detections

This is the rewrite of the Modeling Interface, which provides a system that helps detect the possible and sustaintial exceptions among the giving B UltraSound Images

Project currently is built using poetry and conda to manage the develop currently, see the documentations/build_from_raw_source.md if one would like to setup from blank for developemnt, or see setup.md to browse how to setup from source code.

Switch to the branch old to see the old version of Smart UltraSound Detections, which named Modeling Interface previously.

## Run in Windows

To run the project, you can use the devtools scripts in the root directory as followings

```powershell
devtools.ps1 --all
```

this will help promise the newest ui can be displayed in the application

as a substitude, you can also run the following command without pre-setup environments in the root directory, which is not recommended...

```powershell
devtools.ps1 --run
```

see further help with:

```
powershell.ps1 --help
```


## Run in Linux with bash

To run the project, you can use the devtools scripts in the root directory as followings

```bash
devtools.sh --all
```

this will help promise the newest ui can be displayed in the application

as a substitude, you can also run the following command without pre-setup environments in the root directory, which is not recommended...

```bash
devtools.sh --run
```

see further help with:

```bash
devtools.sh --help
```

## Update Logger

At 2025.1.16: Update logging dependencies, finish setup devtools develop
