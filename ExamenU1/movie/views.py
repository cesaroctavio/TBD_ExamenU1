from django.shortcuts import render

import redis
r = redis.Redis(host='localhost', port=9090, db=0)
# Create your views here.
def home(request):
+    redis.Redis(host='localhost', port=9090, db=0)
+    structure = {
+        "Movies" : { }
+    }
+    count = 0
+    for val in list(Movie.objects.all()):
+        structure["Movies"].update({
+        val.id : {
+            "name": val.name,
+            "year": val.year,
+            "studio": val.studio,
+            "genre": val.genre,
+            "active": val.active,
+            "created": val.created
+        }})
+    return redirect(structure)
