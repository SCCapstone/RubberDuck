@echo off

echo Running autopep on directory...&echo ----------------------------------&echo.

for %%f in (*.py) do (
    echo Running autopep on %%f ...
    Python -m autopep8 --in-place --aggressive --aggressive %%f
    echo %%f formatted using AutoPep8&echo.
)

echo ----------------------------------&echo Checking subdirectories...&echo ----------------------------------&echo.

for /d %%d in (*) do (
    echo %%d
    cd %%d
    echo ----------------------------------
    echo.
    for %%f in (*.py) do (
        echo Running autopep on %%f ...
        Python -m autopep8 --in-place --aggressive --aggressive %%f
        echo %%f formatted using AutoPep8&echo.
    )
    cd ..
)

echo ----------------------------------&echo Finished formatting directory&echo.&echo.


