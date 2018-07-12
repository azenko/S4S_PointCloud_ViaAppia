# S4S_PointCloud_ViaAppia

# Install from source
```bash
$ git clone https://github.com/azenko/S4S_PointCloud_ViaAppia.git
$ cd S4S_PointCloud_ViaAppia
$ docker build . -t azenko/pointcloud
```

# Install from docker
```bash
$ docker pull azenko/pointcloud
```

# Usage
```bash
$ docker run -it -v /data/Via\ Appia/hva/:/input -v $HOME/test:/output azenko/pointcloud build
$ docker run -it -p 9075:9000 -v $HOME/test:/opt/entwine-cesium-pages/data/test azenko/pointcloud serve
```