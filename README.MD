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

Also I added a simple method to draw a sketch of a project. It uses pyplot to draw a polygon of Processing Area (including points themselves as blue circles), GCPs (as red crosses) and polygon created from convex hull of GCPs.
