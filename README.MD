Goal of this project was to parse necessary information from the xml file and find:

1. The number of Ground Control Points (GCPs)
2. The approximate area covered by the GCPs.
3. The effective area covered by the project (processing area)
4. The ratio of these two areas

When with number of Ground Control Points it's clear, my only assumption about the approximate area covered by the GCPs was area of the polygon made of convex hull of the GCPs.
Processing area - just area of polygon.

Project is written in Python 3, thus way to start it would be:

```
  python3 generateCSV.py --project project.p4d --output somefile.csv
```
