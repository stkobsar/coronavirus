# coronavirus
Data analysis of the coronavirus evolution in different countries

## How to use it

    git clone https://github.com/stkobsar/coronavirus.git

    cd coronavirus

    export PYTHONPATH=/path/to/the/folder/you/are/in/

    
## Plot one or several countries evolution of coronavirus

    python coronavirus/main.py --countries "Spain" "Italy" "South Korea"
   

## Plot one country with the different type of data in the data set (total cases by default)

    python coronavirus/main.py -ct "United States" -fld "new_deaths"
    
    python coronavirus/main.py -cts "Slovakia" "Serbia" "Montenegro" -fld "weekly_cases"