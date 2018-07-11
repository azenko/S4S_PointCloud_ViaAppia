# S4S_PointCloud_ViaAppia

# Command to use
```bash
$ cd /data/Via\ Appia/hva
$ find | grep la* |grep -v lax > toMerge.txt
$ ~/tmp/LAStools/bin/las2las -lof toMerge.txt -merged -o mergedData.laz
$ docker run --memory=16g -it -v $HOME:/opt/data -v /data/Via\ Appia/hva:/dataset connormanning/entwine build -i /dataset/mergedData.laz -o /opt/data/entwine/merged-ecef -t 8 -r EPSG:4978
$ docker run --memory=16g -it -v $HOME:/opt/data -v /data/Via\ Appia/hva/drive/:/dataset connormanning/entwine convert -i /opt/data/entwine/merged-ecef -o /opt/data/entwine-cesium-pages/data/merged -t 8 --truncate
```

# Usage
```bash
$ docker run -it -v /data/Via\ Appia/hva/:/input -v $HOME/test:/output testcwine build
$ docker run -it -v $HOME/test:/opt/entwine-cesium-pages/data/test testcwine serve
```