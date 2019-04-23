import os,sys,json,csv,numpy,codecs
from neo4j.v1 import GraphDatabase
from neo4jrestclient.client import GraphDatabase

#CSV FILENAME
csv_path_file_relation_1 = "./FromPlaylistsToTracks.csv"
csv_path_file_relation_2 = "./FromUserToPlaylist.csv"
csv_path_file_node_Playlist = "./PlaylistDistinct.csv"
csv_path_file_node_Track = "./TracksDistinct.csv"
csv_path_file_node_User = "./UsersDistinct.csv"

#FIELDS NAME
playlistToTrackFields = ["from_playlists", "to_tracks"]
userToPlaylistFields = ["from_user", "to_playlist"]
UserFields = ["UserId", "name", "surname", "email"]
PlaylistFields = ["PlaylistId", "Duration","CreatedAt"]
TracksFields = ["TrackId", "ArtistId", "Duration", "Tags"]

def openCsvFile(csv_path_file, *csv_fieldsname):
    with open(csv_path_file, "r") as csvFile:
        csvFileReader = csv.DictReader(csvFile, csv_fieldsname, delimiter=';')
        return csvFileReader

#CONNECT DB
uri = 'localhost'
user = "spotify"
passwd = "C4n3_Bh0"
db = GraphDatabase("http://localhost:7474", username="neo4j", password="C4n3_Bh0")

#CREO SOLO LE LABEL SU NEO4J
user = db.labels.create("User")
playlist = db.labels.create("Playlist")
track = db.labels.create("Track")

#openCsvFile(csv_path_file_node_Playlist, PlaylistFields)
#openCsvFile(csv_path_file_node_Track, TracksFields)
cane = openCsvFile(csv_path_file_node_User, UserFields)
#openCsvFile(csv_path_file_relation_1, playlistToTrackFields)
#openCsvFile(csv_path_file_relation_2, userToPlaylistFields)
print "**************"
print cane

u1 = db.nodes.create()

user.add(u1,u2,u3,un)
#u2 = db.nodes.create(name="Daniela", sur)
#user.add(u2)
#beer = db.labels.create("Beer")
#b1 = db.nodes.create(name="Punk IPA")
#b2 = db.nodes.create(name="Hoegaarden Rosee")

# You can associate a label with many nodes in one go
#beer.add(b1, b2)
