#!/bin/bash

command=$1

case $command in
    # Open the designer
    --open_designer)
        echo "Opening Designer..."
        poetry run python ./dev_tools/open_designer.py
        ;;

    # Summon the UI file
    --summon_uipy)
        echo "Transforming the UI files..."
        poetry run python ./dev_tools/transfer_to_uipy.py ./Ui/MainWindow/MainWindow.ui
        echo "Transforming the UI files done!"
        ;;

    --summon_rccpy)
        echo "Transforming the RCC files..."
        poetry run python ./dev_tools/transfer_rcc_to_py.py ./sources/icons.qrc runtimes_middlewares/rc_py/icons_rc.py
        echo "Transforming the RCC files done!"
        ;;

    # Run the main application
    --run)
        echo "Running main application directly..."
        poetry run python -m smartultrasound_detection.main
        echo "Main application quit"
        ;;

    --prepare)
        echo "Setting up environments for the main application..."
        poetry run python -m smartultrasound_detection.pre_main
        echo "Pre-setup done!"
        ./devtools.sh --summon_rccpy
        ./devtools.sh --summon_uipy
        echo "Setup finished!"
        ;;

    --all)
        ./devtools.sh --prepare
        ./devtools.sh --run
        ;;

    --clean)
        echo "Cleaning the sources..."
        poetry run python -m clean_up.clean
        echo "Clean up done"
        ;;

    --help)
        echo "Usage: devtools.sh [OPTIONS]"
        echo
        echo "Options:"
        echo "    --open_designer        Open Designer and launch the Designer application."
        echo "    --summon_uipy          Summon UI from the .ui file and transform it into the UI Python code."
        echo "    --run                  Run the main application directly."
        echo "    --prepare              Set up environments for the main application and perform necessary transformations."
        echo "    --all                  Set up environments and run the main application."
        echo "    --help                 Show this help message and exit."
        echo "    --clean                Clean up the runtime middlewares and the pycaches"
        ;;

    *)
        echo "Unknown command. Please use one of the following:"
        ./devtools.sh --help
        ;;
esac
