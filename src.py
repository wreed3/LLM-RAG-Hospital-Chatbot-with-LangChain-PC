import polars as pl

HOSPITAL_DATA_PATH = "data/hospitals.csv"
data_hospitals = pl.read_csv(HOSPITAL_DATA_PATH)

print(data_hospitals.shape)
print(data_hospitals.head())

PATIENTS_DATA_PATH = "data/patients.csv"
data_patients = pl.read_csv(PATIENTS_DATA_PATH)

print(data_patients.shape)
print(data_patients.head())

PAYERS_DATA_PATH = "data/payers.csv"
data_payers = pl.read_csv(PAYERS_DATA_PATH)

print(data_payers.shape)
print(data_payers.head())

PHYSICIAN_DATA_PATH = "data/physicians.csv"
data_physician = pl.read_csv(PHYSICIAN_DATA_PATH)

print(data_physician.shape)

print(data_physician.head())


REVIEWS_DATA_PATH = "data/reviews.csv"
data_reviews = pl.read_csv(REVIEWS_DATA_PATH)

print(data_reviews.shape)
print(data_reviews.head())

VISITS_DATA_PATH = "data/visits.csv"
data_visits = pl.read_csv(VISITS_DATA_PATH)

print(data_visits.shape)
print(data_visits.head())
