import requests
from datetime import datetime

USERNAME = "misiaty"
TOKEN = "MisiatyMateusz"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
headers = {"X-USER-TOKEN": TOKEN}

# # # Creating user on the platform

# pixela_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
# responce = requests.post(url=pixela_endpoint, json=pixela_params)
# print(responce.text)


# # # Creating graph on Pixela webside

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# graph_config = {
#     "id": GRAPH_ID,
#     "name": "Learning Graph",
#     "unit": "h",
#     "type": "float",
#     "color": "ichou",
# }

# pixela_graph_response = requests.post(
#     url=graph_endpoint, json=graph_config, headers=headers
# )

# print(pixela_graph_response.text)


# Changing input date into formated date
def get_date():
    updated_day, updated_month, updated_year = input(
        "Give a date to update\nFormat: Year Month Day (example: 01 08 2021)\n>> "
    ).split()
    date = updated_year + updated_month + updated_day
    return date


# Adding pixel to habit tracker with value gived in input
def add_today_value():
    # Getting todays date
    now = datetime.now()
    date = now.strftime("%Y%m%d")

    learning_time = input("How much did you study today?\n>> ").replace(",", ".")

    pixela_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

    pixel_config = {"date": date, "quantity": learning_time}

    add_pixel_response = requests.post(
        url=pixela_pixel_endpoint, json=pixel_config, headers=headers
    )

    print(add_pixel_response.text)


# Updating value in pixel respodnig for given date
def update_previous_value():
    date = get_date()
    update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"

    quantity = input("Value:\n>> ").replace(",", ".")
    update_pixel_config = {"quantity": quantity}

    updated_pixel_response = requests.put(
        url=update_pixel_endpoint, json=update_pixel_config, headers=headers
    )

    print(updated_pixel_response.text)


# Deleting pixel value in given date
def delete_value():
    date = get_date()
    delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"

    delete_response = requests.delete(url=delete_pixel_endpoint, headers=headers)

    print(delete_response.text)


command = input(
    "What do you want to do with your habit tracker?\n(add_today_value / update_previous_value / delete_value)\n>> "
).strip()

if command == "add_today_value":
    add_today_value()

elif command == "update_previous_value":
    update_previous_value()
elif command == "delete_value":
    delete_value()
else:
    print("I do not recognize this command")
