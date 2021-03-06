# <p align = "center"> Mining patterns from songs banned after the 9/11 </p> 
Final project of the course of Computational Social Sciences at the University of Trento (A.Y. 2020/2021) and aims at mining patterns from songs banned after the 9/11. 

---
## Prerequisites
In order to run this project, the following tools have to be installed on your machine:

- Python, preferably 3.8 or newer 
- R and, for visualizations, the IDE [RStudio](https://www.rstudio.com/)

## Installation 

### Clone the repository 

Clone this repository in a local directory typing in the command line: 

```
git clone https://github.com/elypaolazz/BDT-Project.git
```

## Usage

### 1 Data Collection
The data collection follows a two steps procedure.

#### Genius API and Spotify API implemented in Python.
The script connects via the [Spotify API](https://developer.spotify.com/documentation/web-api/) to the user account and downloads id’s,
artist name(s), and track title of the chosen playlist:

- CSS project

- CSS 2000

Using the song title and artist name, the songs are searched in the collection
of [Genius.com](https://genius.com/). If the song is found, its lyrics is downloaded and stored in a csv
file together with the corresponding Spotify track id.

#### Spotify API implemented in R
The script connects via Spotify API to the user account and downloads all
possible data from the chosen playlist. However, the download is limited to
100 songs. The data is stored in an R data frame and joined with the csv file
containing the lyrics.

### 2 Before running the code
#### 2.1. Authentication
To run the code, the personal access keys for Spotify API and Genius API are
necessary. Below are reported the necessary keys:
- *SPOTIFY CLIENT ID* = ’my_key’
- *SPOTIFY CLIENT SECRET* = ’my_key’
- *Account name* = ’my_name’
- *GENIUS KEY* = ’genius_key’

#### 2.2 Find the playlists
The playlists are publicly available at the following links:

- CSS_project: https://open.spotify.com/playlist/6lAzVorsMoZq3vSYQ01L1y?si=a623926e15c74b4e
- CSS_2000: https://open.spotify.com/playlist/3Ir7lPTD9niR2MFLGwi8Kg?si=366795b559e54d87

Before the download, the playlists must be saved within the playlists of the user.
