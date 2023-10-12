import csv
import datetime
import matplotlib.pyplot as plt

def load_data(start_date=None, end_date=None):
    try:
        with open('data.csv', 'r') as file:
            reader = csv.DictReader(file)
            data = []
            start_date = datetime.datetime.strptime(start_date, '%d/%m/%Y').date()
            end_date = datetime.datetime.strptime(end_date, '%d/%m/%Y').date()
            for row in reader:
                date_created = datetime.datetime.strptime(row['date_created'], '%Y-%m-%d %H:%M:%S.%f %z').date()
                if start_date and end_date:
                    if start_date <= date_created <= end_date:
                        data.append(row)
                else:
                    data.append(row)
            return data
    except FileNotFoundError:
        print("File 'data.csv' not found.")
        return []
    except KeyError:
        print("Invalid column names in 'data.csv'. Please check the column names.")
        return []
    except ValueError:
        print("Invalid date format. Please use the format 'dd/mm/yyyy' for start_date and end_date.")
        return []

def calculate_outstanding_per_building(data):
    outstanding = {}
    for row in data:
        building_id = row['buildingID']
        if row['plirothike'] == '0':
            expense = float(row['poso'])
            if building_id not in outstanding:
                outstanding[building_id] = expense
            else:
                outstanding[building_id] += expense
    return outstanding

def plot_outstanding_per_building(outstanding):
    if not outstanding:
        print("No data available for plotting.")
        return

    building_ids = list(outstanding.keys())
    outstanding_amounts = list(outstanding.values())

    plt.bar(building_ids, outstanding_amounts)
    plt.xlabel('Building ID')
    plt.ylabel('Outstanding Amount')
    plt.title('Outstanding Amount per Building')
    plt.xticks(rotation=90)
    plt.show()

def plot_monthly_outstanding_per_building(data):
    if not data:
        print("No data available for plotting.")
        return

    months = {}
    for row in data:
        building_id = row['buildingID']
        date_created = row['date_created'].split()[0]

        if row['plirothike'] == '0':
            if building_id not in months:
                months[building_id] = {}

            if date_created not in months[building_id]:
                months[building_id][date_created] = 0

            months[building_id][date_created] += float(row['poso'])

    if not months:
        print("No data available for plotting.")
        return

    for building_id, monthly_data in months.items():
        months_sorted = sorted(monthly_data.keys(), key=lambda x: datetime.datetime.strptime(x, '%m/%Y'))
        months_sorted = [datetime.datetime.strptime(month, '%m/%Y').date() for month in months_sorted]

        amounts = [monthly_data[month] for month in months_sorted]

        plt.plot(months_sorted, amounts, label=f'Building {building_id}')

    plt.xlabel('Month')
    plt.ylabel('Outstanding Amount')
    plt.title('Monthly Outstanding Amount per Building')
    plt.legend()
    plt.xticks(rotation=90)
    plt.show()

import csv
import datetime
import matplotlib.pyplot as plt

def load_data(start_date=None, end_date=None):
    try:
        with open('data.csv', 'r') as file:
            reader = csv.DictReader(file)
            data = []
            start_date = datetime.datetime.strptime(start_date, '%d/%m/%Y').date()
            end_date = datetime.datetime.strptime(end_date, '%d/%m/%Y').date()
            for row in reader:
                date_created = datetime.datetime.strptime(row['date_created'], '%Y-%m-%d %H:%M:%S.%f %z').date()
                if start_date and end_date:
                    if start_date <= date_created <= end_date:
                        data.append(row)
                else:
                    data.append(row)
            return data
    except FileNotFoundError:
        print("File 'data.csv' not found.")
        return []
    except KeyError:
        print("Invalid column names in 'data.csv'. Please check the column names.")
        return []
    except ValueError:
        print("Invalid date format. Please use the format 'dd/mm/yyyy' for start_date and end_date.")
        return []

def calculate_outstanding_per_building(data):
    outstanding = {}
    for row in data:
        building_id = row['buildingID']
        if row['plirothike'] == 'false':
            expense = float(row['poso'])
            if building_id not in outstanding:
                outstanding[building_id] = expense
            else:
                outstanding[building_id] += expense
    return outstanding

def plot_outstanding_per_building(outstanding):
    if not outstanding:
        print("No data available for plotting.")
        return
    else:

        building_ids = list(outstanding.keys())
        outstanding_amounts = list(outstanding.values())

        plt.bar(building_ids, outstanding_amounts)
        plt.xlabel('Building ID')
        plt.ylabel('Outstanding Amount')
        plt.title('Outstanding Amount per Building')
        plt.xticks(rotation=90)
        plt.show()

def plot_monthly_outstanding_per_building(data):
    if not data:
        print("No data available for plotting.")
        return

    months = {}
    for row in data:
        building_id = row['buildingID']
        date_created = row['date_created'].split()[0]

        if row['plirothike'] == False:
            if building_id not in months:
                months[building_id] = {}

            if date_created not in months[building_id]:
                months[building_id][date_created] = 0

            months[building_id][date_created] += float(row['poso'])

    if not months:
        print("No data available for plotting.")
        return

    for building_id, monthly_data in months.items():
        months_sorted = sorted(monthly_data.keys(), key=lambda x: datetime.datetime.strptime(x, '%Y/%m/%d'))
        months_sorted = [datetime.datetime.strptime(month, '%Y/%m/%d').date() for month in months_sorted]

        amounts = [monthly_data[month] for month in months_sorted]

        plt.plot(months_sorted, amounts, label=f'Building {building_id}')

    plt.xlabel('Month')
    plt.ylabel('Outstanding Amount')
    plt.title('Monthly Outstanding Amount per Building')
    plt.legend()
    plt.xticks(rotation=90)
    plt.show()

def plot_expenses_per_building(data):
    if not data:
        print("No data available for plotting.")
        return

    building_expenses = {}
    for row in data:
        building_id = row['buildingID']
        expense = float(row['poso'])
        if building_id not in building_expenses:
            building_expenses[building_id] = expense
        else:
            building_expenses[building_id] += expense

    if not building_expenses:
        print("No data available for plotting.")
        return

    building_ids = list(building_expenses.keys())
    total_expenses = list(building_expenses.values())

    plt.bar(building_ids, total_expenses)
    plt.xlabel('Building ID')
    plt.ylabel('Total Expenses')
    plt.title('Expenses per Building')
    plt.show()


# Load data
start_date = "01/01/2023"
end_date = "31/12/2024"
data = load_data(start_date, end_date)

# Calculate outstanding per building
outstanding_per_building = calculate_outstanding_per_building(data)

# Plot outstanding per building
plot_outstanding_per_building(outstanding_per_building)

# Plot monthly outstanding per building
plot_monthly_outstanding_per_building(data)

# Plot expenses per building
plot_expenses_per_building(data)