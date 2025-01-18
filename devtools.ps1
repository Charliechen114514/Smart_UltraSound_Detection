param (
    [string]$command
)

switch ($command) {
    # Open the designer 
    "--open_designer" {
        Write-Host "Opening Designer..."
        poetry run python .\dev_tools\open_designer.py
    }

    # summon the ui file
    "--summon_uipy" {
        Write-Host "transforming the ui files..."
        poetry run python .\dev_tools\transfer_to_uipy.py .\Ui\MainWindow\MainWindow.ui
        poetry run python .\dev_tools\transfer_to_uipy.py .\Ui\BrowsingGuide\BrowsingGuide.ui
        poetry run python .\dev_tools\transfer_to_uipy.py .\Ui\InfoWindow\InfoWindow.ui
        Write-Host "transforming the ui files done!"
    }

    "--summon_rccpy" {
        Write-Host "transforming the rcc files..."
        poetry run python .\dev_tools\transfer_rcc_to_py.py .\sources\icons.qrc runtimes_middlewares\rc_py\icons_rc.py
        Write-Host "transforming the rcc files done!"
    }

    # run the main applications
    "--run" {   
        Write-Host "Running main application directly..."
        poetry run python -m smartultrasound_detection.main
        Write-Host "main application quit"
    }

    "--prepare"{
        Write-Host "setup environments for the main application..."
        poetry run python -m smartultrasound_detection.pre_main
        Write-Host "pre-setup down!"
        devtools.ps1 --summon_rccpy
        devtools.ps1 --summon_uipy
        Write-Host "setup finished!"
    }

    "--all"{
        devtools.ps1 --prepare
        devtools.ps1 --run
    }

    "--clean"{
        Write-Host "Cleaning the sources..."
        poetry run python -m clean_up.clean
        Write-Host "Clean up down"
    }

    "--train"{
        Write-Host "Start training the model"
        poetry run python -m model_train.model_train
        Write-Host "Model train down, check the train folder for the usage"
    }

    "--test"{
        Write-Host "Test the main functionalities..."
        poetry run pytest
        Write-Host "Test Donw"
    }

    "--help"{
        Write-Host 

    "Usage: devtools.ps1 [OPTIONS]

    Options:
        --open_designer        Open Designer and launch the Designer application.
        --summon_uipy          Summon UI from the .ui file and transform it into the UI Python code.
        --run                  Run the main application directly.
        --prepare              Set up environments for the main application and perform necessary transformations.
        --all                  Set up environments and run the main application.
        --help                 Show this help message and exit.
        --clean                Clean up the runtime middlewares and the pycaches
        --test                 Test the functionalities if required
        "  
        
    }

    default {
        Write-Host "Unknown command. Please use one of the following:"
        dev_tools.ps1 --help
    }
}
