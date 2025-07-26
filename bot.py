"""
WARNING:

Please make sure you install the bot dependencies with `pip install --upgrade -r requirements.txt`
in order to get all the dependencies on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the dependencies.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install --upgrade -r requirements.txt`
- Use the same interpreter as the one used to install the bot (`pip install --upgrade -r requirements.txt`)

Please refer to the documentation for more information at
https://documentation.botcity.dev/tutorials/python-automations/desktop/
"""

# Import for the Desktop Bot
from botcity.core import DesktopBot

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = DesktopBot()
    
    # Implement here your logic..
    path_fakturama = r"C:\Program Files\Fakturama2\Fakturama.exe"

    produtos = [
        {
            "Item Number": 1,
            "Name": "Laptop",
            "Category": "Eletrônico",
            "GTIN": "1234567890123",
            "Supplier Code": "SUP001",
            "Description": "Alto desempenho com as últimas especificações.",
            "Price": 999.99,
            "Cost Price": 799.99,
            "Allowance": 50,
            "Stock": 100
        },
        {
            "Item Number": 2,
            "Name": "Smartphone",
            "Category": "Eletrônico",
            "GTIN": "9876543210987",
            "Supplier Code": "SUP002",
            "Description": "Smartphone com recursos avançados de câmera e display.",
            "Price": 699.99,
            "Cost Price": 549.99,
            "Allowance": 30,
            "Stock": 150
        },
        {
            "Item Number": 3,
            "Name": "Tenis de corrida",
            "Category": "Esporte",
            "GTIN": "7654321098765",
            "Supplier Code": "SUP003",
            "Description": "Confortável e resistente, ideal para corridas.",
            "Price": 89.99,
            "Cost Price": 69.99,
            "Allowance": 20,
            "Stock": 200
        }
    ]

    bot.execute(path_fakturama)

    for produto in produtos:

        # Searching for element 'new_product'
        if not bot.find("new_product", matching=0.97, waiting_time=10000):
            not_found("new_product")
        bot.click()
        
        # Searching for element 'item_number'
        if not bot.find("item_number", matching=0.97, waiting_time=10000):
            not_found("item_number")
        bot.click_relative(88, 9)

        bot.paste(produto['Item Number'])
        
        bot.tab()

        bot.paste(produto['Name'])

        bot.tab()

        bot.paste(produto['Category'])

        bot.tab()

        bot.paste(produto['GTIN'])

        bot.tab()

        bot.paste(produto['Supplier Code'])
        
        bot.tab()

        bot.paste(produto['Description'])

        bot.tab()

        bot.paste(produto['Price'])

        bot.tab()

        bot.paste(produto['Cost Price'])

        bot.tab()

        bot.paste(produto['Allowance'])

        bot.tab()
        bot.tab()

        bot.paste(produto['Stock'])

        bot.control_s()

        bot.control_w()
    
    bot.alt_f4()





   

        

    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK.",
    #     total_items=0,
    #     processed_items=0,
    #     failed_items=0
    # )

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()