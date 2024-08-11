### August 8, 2024
* Brief introudction
* IDE and Code setup
* Data collection (what type we need)
    * take your own personal pictures to use as data
    * Use the Roboflow coffee dataset -> use tensorflow as well
* https://universe.roboflow.com/cuenta-6/cafelitos/images/FUyrnK6Q79nwMNfyXQTS?queryText=&pageSize=50&startingIndex=0&browseQuery=true
    * Download code for the dataset above

    ```
    !pip install roboflow
    from roboflow import Roboflow
    rf = Roboflow(api_key="Kn5Q5bgVfMIFcPUy0znL")
    project = rf.workspace("california-state-polytechnic-univeresity-of-pomona").project("cafelitos-4nj9z")
    version = project.version(1)
    dataset = version.download("yolov8")
    ```

### August 10, 2024
* There are multiple ways to handle the data
* However, focus on the goal of being able to measure the caffeine levels through an image of coffee
    * Not all coffees are the same size
    * Sometimes, the image of coffee will also include the cup (different colors)
    * Even if you scale all the images to the same size so that the image procesing algorithm can analyze it, there will be "background noise" or "unecessary data"