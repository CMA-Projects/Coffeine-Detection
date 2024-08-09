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
