import csv

data = []
data_sort = []
clean_data = []
 
def csv_reader(f):
    reader = csv.reader(f)
    for row in reader:
        data.append(row)

def csv_writer(data, path):
    with open(path, "w", newline='', encoding="utf-8") as f:
        w = csv.writer(f, dialect='excel',delimiter=',')
        for i in data:
            w.writerow(i)
 
if __name__ == "__main__":
    csv_path = "dataset_isp.csv"
    with open(csv_path, "r") as f:
        csv_reader(f)

    for i in range(len(data)):
        if data[i][3:4] == ['legit']:
            data_sort.append(data[i][1:5])

    for i in range(len(data_sort)):
        if len(data_sort[i][0].split(".")) == 2:
            clean_data.append(data_sort[i])

    csv_writer(clean_data, "C:/Users/Klime/Desktop/Model.csv")
    #print(clean_data)

    # print(len(data))
    # print(len(data_sort))
    # print(len(clean_data))
