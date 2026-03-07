
CREATE TABLE IF NOT EXISTS dive_sites (
    ID INTEGER PRIMARY KEY,
    Name TEXT,
    Latitude REAL,
    Longitude REAL,
    "Water Temperature" TEXT,
    "Skill Level" TEXT,
    "Depth Range" TEXT,
    Description TEXT,
    Visibility TEXT,
    "Best Time" TEXT,
    Region TEXT,
    "Marine Life" TEXT,
    Hazards TEXT,
    Facilities TEXT,
    "Image URL" TEXT,
    Featured BOOLEAN,
    "Created At" TEXT,
    "Viz Slug" TEXT,
    "Compass Bearing" TEXT,
    "Nearby Runoff" TEXT,
    "Viz Triggers" TEXT,
    "Viz Seasonal" TEXT
);

.mode csv
.import scubadownunder.csv dive_sites
