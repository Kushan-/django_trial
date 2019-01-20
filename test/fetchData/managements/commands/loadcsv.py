from csv import DictReader
import pymongo

connection = pymongo.MongoClient('ds153814.mlab.com', 53814);
db = connection['djangotest']
db.authenticate('kush', '!TeddyH.0')

collection = db['dogsDB']
print(db.list_collection_names())
for row in DictReader(open('./dogs.csv')):
    print(row['dog_name'], row['gender'], row['breed'], row['birth'], row['dominant_color'], row['secondary_color'], row['third_color'], row['spayed_or_neutered'], row['guard_or_trained'], row['borough'], row['zip_code'])
    mydict = {'dog_name':row['dog_name'], "gender":row['breed'], "birth":row['birth'], 'dominant_color':row['dominant_color'],
                "secondary_color":row["secondary_color"], "third_color":row["third_color"], 'spayed_or_neutered':row['spayed_or_neutered'],
               'guard_or_trained': row['guard_or_trained'], 'borough':row['borough'], 'zip_code':row['zip_code']
            }
    collection.insert_one(mydict)

#             DogsData.dog_name = row['dog_name']
#             DogsData.gender = row['gender']
#             DogsData.breed = row['breed']
#             DogsData.birth = row['birth']
#             DogsData.dominant_color = row['dominant_color']
#             DogsData.secondary_color = row['secondary_color']
#             DogsData.third_color = row['third_color']
#             DogsData.spayed_or_neutered = row['spayed_or_neutered']
#             DogsData.guard_or_trained = row['guard_or_trained']
#             DogsData.borough = row['borough']
#             DogsData.zip_code = row['zip_code']


# from datetime import datetime

# from django.core.management import BaseCommand

# from fetchData.models import DogsData
# from pytz import UTC


# DATETIME_FORMAT = '%m/%d/%Y %H:%M'

# VACCINES_NAMES = [
#     'Canine Parvo',
#     'Canine Distemper',
#     'Canine Rabies',
#     'Canine Leptospira',
#     'Feline Herpes Virus 1',
#     'Feline Rabies',
#     'Feline Leukemia'
# ]

# ALREADY_LOADED_ERROR_MESSAGE = """
# If you need to reload the pet data from the CSV file,
# first delete the db.sqlite3 file to destroy the database.
# Then, run `python manage.py migrate` for a new empty
# database with tables"""


# class Command(BaseCommand):
#     # Show this when the user types help
#     help = "Loads data from dogs.csv into our Pet model"

#     def handle(self, *args, **options):
#         if DogsData.objects.exists():
#             print('Pet data already loaded...exiting.')
#             print(ALREADY_LOADED_ERROR_MESSAGE)
#             return
#         print("Creating vaccine data")
        
#         for row in DictReader(open('./dogs.csv')):
#             DogsData = DogsData()
#             DogsData.dog_name = row['dog_name']
#             DogsData.gender = row['gender']
#             DogsData.breed = row['breed']
#             DogsData.birth = row['birth']
#             DogsData.dominant_color = row['dominant_color']
#             DogsData.secondary_color = row['secondary_color']
#             DogsData.third_color = row['third_color']
#             DogsData.spayed_or_neutered = row['spayed_or_neutered']
#             DogsData.guard_or_trained = row['guard_or_trained']
#             DogsData.borough = row['borough']
#             DogsData.zip_code = row['zip_code']
#             DogsData.save()


'''

    dog_name = models.CharField(max_length=20, null=True)
    gender = models.CharField(choices=SEX_CHOICES, max_length=1, null=True)
    breed = models.CharField(max_length=30, blank=True)
    birth = models.DateTimeField(auto_now_add=False, auto_now=False)
    dominant_color = models.CharField(max_length=20, blank=False)
    secondary_color = models.CharField(max_length=20, blank=True)
    third_color = models.CharField(max_length=20, blank=True)
    spayed_or_neutered = models.CharField(choices=spayed_or_neutered_CHOICE, max_length=1, null=True)
    guard_or_trained = models.CharField(choices=spayed_or_neutered_CHOICE, max_length=1, null=True)
    borough = models.CharField(max_length=30, blank=False, null=False)
    zip_code = models.IntegerField(null=False)

'''
