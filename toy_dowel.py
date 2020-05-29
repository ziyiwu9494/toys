import csv

# to_csv = {'foo': 1, 'bar': 10, }
#
# writer = csv.DictWriter(open('out.csv', 'w+'), fieldnames=set(to_csv.keys()), extrasaction='ignore')
# writer.writeheader()
#
# writer.writerow(to_csv)
#
file = open('out.csv', 'r+')


def add_row(to_csv):
    rewrite_csv = list()
    reader = csv.DictReader(file)
    fieldnames = reader.fieldnames
    for row in reader:
        for key in to_csv.keys():
            if key not in fieldnames:
                row[key] = ''
        rewrite_csv.append(dict(row))
    rewrite_csv.append(to_csv)
    writer = csv.DictWriter(file, fieldnames=set(to_csv.keys()), extrasaction='ignore')
    file.seek(0)
    writer.writeheader()
    writer.writerows(rewrite_csv)
    file.truncate()


add_row({'foo': 1, 'baz': 10})
# writer.writerow(to_csv)
