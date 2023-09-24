import csv


data = [
    ("EMAIL", "moyinoluwjohnson2@gmail.com"),
    ("EMAIL", "Steveuche404@gmail.com"),
    ("EMAIL", "Pelumioke02@gmail.com"),
    ("EMAIL", "ebukaegbunike@gmail.com"),
    ("EMAIL", "adelekeyahaya05@gmail.com"),
    ("EMAIL", "cryptotech024@gmail.com"),
    ("EMAIL", "oyegbilemarvellous@yahoo.com"),
    ("EMAIL", "Uarmyjhohpy@gmail.com"),
    ("EMAIL", "Cryptogeniuz4@gmail.com"),
    ("EMAIL", "babatopeolowokere@yahoo.com"),
    ("EMAIL", "fafunmiolusegun@gmail.com"),
    ("EMAIL", "seyialawuh@gmail.com"),
    ("EMAIL", "damilaresamuelg6@gmail.com"),
    ("EMAIL", "mzzbaunigel@gmail.com"),
    ("EMAIL", "wakawaemmanuel451@gmail.com"),
    ("EMAIL", "ajufoudenna@gmail.com"),
    ("EMAIL", "youngdan947@gmail.com"),
    ("EMAIL", "imiainfo.ca@gmail.com"),
    ("EMAIL", "victorafia13@gmail.com"),
    ("EMAIL", "sikemiomotola@gmail.com"),
    ("EMAIL", "odukoyaayomide674@gmail.com"),
    ("EMAIL", "nagelgerrit@kpnmail.nl"),
    ("EMAIL", "joezy1995@gmail.com"),
    ("EMAIL", "peterglo2200@gmail.com"),
    ("EMAIL", "perekosufaobudah08@gmail.com"),
    ("EMAIL", "ericsingler7@gmail.com"),
    ("EMAIL", "ayodejitomiwa318@gmail.com"),
    ("EMAIL", "agbajepamilerin100@gmail.com"),
    ("EMAIL", "sisiitunu@gmail.com"),
    ("EMAIL", "jabulanietokakpan@gmail.com"),
    ("EMAIL", "bankolefestusb@gmail.com"),
    ("EMAIL", "easykiddathawonderkind@gmail.com"),
    ("EMAIL", "abejeremiah98@gmail.com"),
    ("EMAIL", "mofoluwasewaeludoyin@gmail.com"),
    ("EMAIL", "onukwilio@gmail.com"),
    ("EMAIL", "davidologe1@gmail.com"),
    ("EMAIL", "quamejunior@gmail.com"),
    ("EMAIL", "praiseskelz@gmail.com"),
    ("EMAIL", "olaitanminkail100@gmail.com"),
    ("EMAIL", "universomahalaksmi@gmail.com"),
    ("EMAIL", "jamesconnor08154@gmail.com"),
    ("EMAIL", "dylanjthomas2001outlook.com"),
    ("EMAIL", "kealdy001@gmail.com"),
    ("EMAIL", "Oluwanisholaolaoluwa@gmail.com"),
    ("EMAIL", "Ifeenwosu23@gmail.com"),
    ("EMAIL", "jossyatam@gmail.com"),
    ("EMAIL", "Visiondaniels32@gmail.com"),
    ("EMAIL", "lmnjfar@gmail.com"),
    ("EMAIL", "oluwalalakaisraelt@gmail.com"),
    ("EMAIL", "segunath98@gmail.com"),
    ("EMAIL", "loliahodan@gmail.com"),
    ("EMAIL", "philipnkwam@gmail.com"),
    ("EMAIL", "adewapswaps@gmail.com"),
    ("EMAIL", "patriciaogboo@gmail.com"),
    ("EMAIL", "mohamed.ayered4@gmail.com"),
    ("EMAIL", "olowoyiribimiracle@gmail.com"),
    ("EMAIL", "bernerdezra112@gmail.com"),
    ("EMAIL", "mercieojo@gmail.com"),
    ("EMAIL", "dammygee492@gmail.com"),
    ("EMAIL", "eunithelp@gmail.com"),
    ("EMAIL", "chibuuzoeshi@gmail.com"),
    ("EMAIL", "misheleuba@gmail.com"),
    ("EMAIL", "joshuaadejola@gmail.com")
]

# Define the CSV file path
csv_file = "email_data.csv"

# Write data to the CSV file
with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["ChannelType", "Address"])  # Write the column headers
    writer.writerows(data)  # Write the data rows
