# UNDER CONSTRUCTION !!!  
# (but it seems to work)

# Prepare a Docker image  
# for use in building ffmpeg  
# in a NEW disposable/re-usable docker container  



0. Setup  
0.1 Install docker from ```https://docs.docker.com/docker-for-windows/install/``` and configure it.  
0.2 This is important:  notice ```-v D:/VM:/VM``` in the docker commandline,
as it permits copying of newly built ffmpeg executables back to the host machine.  
Outside of Docker, first ensure that the files in our git 
subfolder ```/docker/app/``` are copied to a place where the docker 
scripts can copy them from. An example of this not shown.  
In the instructions below, we had already copied the files to ```D:\VM\docker\app```
... notice that inside the docker container ```/VM``` will thus be 
mapped to ```D:/VM``` via the docker ```RUN``` commandline.  

1. Create a new docker container based on ubuntu in the public repository
```
docker container -a
docker run -i -t --attach STDIN --attach STDOUT --attach STDERR -v D:/VM:/VM ubuntu
```

2. Update the container by installing dependencies (excluding MingW etc).  
```
cd /
cp -fv /VM/docker/app/* ./
chmod +777 ./*.sh
./run_prep.sh
# answer any prompted questions
exit
```

3. Save the container to a new image called ubuntu_build_ffmpeg:ubuntu_build_ffmpeg_base
```
docker container ps -a
docker image ls -a
docker commit <the_container_id> ubuntu_build_ffmpeg_base:ubuntu_build_ffmpeg_base
```

4. Create a new docker container based on ubuntu_build_ffmpeg_base
```
docker run -i -t --attach STDIN --attach STDOUT --attach STDERR -v D:/VM:/VM ubuntu_build_ffmpeg_base:ubuntu_build_ffmpeg_base
```

5. Update the container with MingW and GCC etc by running ffmpeg build once
```
cd /
chmod +777 ./*.sh
./h3333_v100.001.sh
exit
```

6. Save the container to a new image
```
docker container ps -a
docker image ls -a
docker commit <the_container_id> ubuntu_build_ffmpeg_with_mingw:ubuntu_build_ffmpeg_with_mingw
```

7. Later, to re-build ffmpeg, 
```
docker run -i -t --attach STDIN --attach STDOUT --attach STDERR -v D:/VM:/VM ubuntu_build_ffmpeg_with_mingw:ubuntu_build_ffmpeg_with_mingw
cd /
chmod +777 ./*.sh
./h3333_v100.001.sh
exit
```
**and the resulting new executable files should exist in folder ```D:\VM\exe_x64_py\```**  

8. If one needs to re-build a replacement image with a new version of MingW/GCC etc, simply   
8.1 ensure all docker containers are stopped  
8.2 docker image rm ubuntu_build_ffmpeg_with_mingw (or possibly use it's <container_id>)  
8.3 repeat steps 4. through 6. inclusive  

9. Now that we have a reliable docker container, we can (re)build ffmpeg any time
by doing step 7.
