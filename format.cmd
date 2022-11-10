@echo off

echo Running yapf on directory...&echo ----------------------------------&echo.

for %%f in (*.py) do (
    echo Running yapf on %%f ...
    Python -m yapf --in-place --recursive --style="{indent_width: 4}" %%f
    echo %%f formatted using yapf&echo.
)

echo ----------------------------------&echo Checking subdirectories...&echo ----------------------------------&echo.

for /d %%d in (*) do (
    echo %%d
    cd %%d
    echo ----------------------------------
    echo.
    for %%f in (*.py) do (
        echo Running yapf on %%f ...
        Python -m yapf --in-place --recursive --style="{indent_width: 4}" %%f
        echo %%f formatted using yapf&echo.
    )
    cd ..
)

echo ----------------------------------&echo Finished formatting directory&echo.&echo.


