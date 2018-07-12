# S4S_PointCloud_ViaAppia
[![DOI](https://zenodo.org/badge/140538217.svg)](https://zenodo.org/badge/latestdoi/140538217)

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

# For Demo
```bash
$ docker run -it -m 32g --cpus=16 -v /data/rrsources:/input -v /data/red-rocks:/output azenko/pointcloud build
$ docker run -it -p 8080:9000 -v /data/:/opt/entwine-cesium-pages/data/ azenko/pointcloud serve

$ docker run -it -m 32g --cpus=16 -v /data/hwsources:/input -v /data/kauai:/output azenko/pointcloud build
$ docker run -it -p 8080:9000 -v /data/:/opt/entwine-cesium-pages/data/ azenko/pointcloud serve
```