# DroneKit İle Drone Programlama

![Black and White Minimalist Gaming Channel Banner Landscape](https://github.com/AhmetBeratKocyigit/DroneKit/assets/135528027/e1ef9433-0efa-4ac1-a8cc-9c2347cb450f)

- - -

# Sanal Makinaya Ubuntu Kurmak

DroneKit kütüphanesi kullanmak için öncelikle Ubuntu işletim sistemine sahip bir bilgisayara ihtiyaç duyuyoruz. Windows işletim sisteminde sanal bilgisayar yazılımları ile bu ihtiyacımızı karşılıyabiliyoruz

VMware programının setup dosyasını indirmek için : https://www.vmware.com/products/workstation-player/workstation-player-evaluation.html

Ubuntu işletim sisteminin İSO dosyasını indirmek için : https://releases.ubuntu.com/18.04.6/?_ga=2.59504109.1117219064.1700847152-2047495795.1700847152

Video : https://youtu.be/RoPxb5IMolQ

- - -

# Gerekli Programların Kurulması

DroneKit ile drone programlama için gerekli olan programlar

* Ardupilot SITL

* Gazebo

* DroneKit

- - -

## Ardupilot SITL

ArduPilot Herhangi Bir Ek Donanım Olmadan Uçuşları Simüle Edebilmemizi Sağlıyor

Ardupilot SITL programını kurmak için öncelikle Git'i kurmamız gerekiyor

Video : https://youtu.be/s6PudIehiRc

### Git Kurulumu

```bash
sudo apt-get update
```

```bash
sudo apt-get upgrade
```


```bash
sudo apt-get install git
```

```bash
sudo apt-get install gitk git-gui
```

### Git üzerinden Ardupilot SITL dosyalarını indirme

```bash
git clone https://github.com/ArduPilot/ardupilot.git
```

### Gerekli Bileşenlerin Yüklenmesi

```bash
cd ardupilot
```

```bash
git submodule update --init --recursive
```

```bash
sudo apt install python-matplotlib python-serial python-wxgtk4.0 python-wxtools
python-lxml python-scipy python-opencv ccache gawk python-pip python-pexpect

```

```bash
gedit ~/.bashrc
```
.bashrc dosyası açıldıktan sonra en alt satıra inerek alttaki iki satırı yapıştırmanız gerekiyor

```bash
export PATH=$PATH:$HOME/ardupilot/Tools/autotest
export PATH=/usr/lib/ccache:$PATH
```


```bash
. ~/.bashrc
```

```bash
sudo pip install future pymavlink MAVProxy
```

### Ve Son Olarak Programın Çalıştırılması

```bash
cd ~/ardupilot/ArduCopter
```

```bash
  ../Tools/autotest/sim_vehicle.py -w --console --map
```

- - -

## Gazebo

Video : https://youtu.be/meYmYmBanPU

Gerekli İzinlerin Ayarlanması

```bash
sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'
```

```bash
wget https://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -
```

Gazebo Programının Kurulumu

```bash
sudo apt update
```

```bash
sudo apt-get install gazebo9
```

```bash
sudo apt-get install libgazebo9-dev
```

ArduPilot Eklentisinin Kurulması

```bash
git clone https://github.com/khancyr/ardupilot_gazebo
```

```bash
cd ardupilot_gazebo
```

```bash
mkdir build
```

```bash
cd build
```

```bash
cmake ..
```

```bash
make -j4
```

```bash
sudo make install
```

```bash
echo 'source /usr/share/gazebo/setup.sh' >> ~/.bashrc
```

```bash
echo 'export GAZEBO_MODEL_PATH=~/ardupilot_gazebo/models' >> ~/.bashrc
```

Gazebo sanal makinede hata verirse aşağıdaki kodu terminalde çalıştırarak hatayı giderebilirsiniz.

```bash
export SVGA_VGPU10=0
```

```bash
echo "export SVGA_VGPU10=0" >> ~/.bashrc
```

Vee Son Olarak Programı Çalıştırmak 

```bash
gazebo --verbose worlds/iris_arducopter_runway.world
```

```bash
cd ~/ardupilot/ArduCopter
```

```bash
../Tools/autotest/sim_vehicle.py -f gazebo-iris --console --map
```

- - -

## DroneKit Kurulumu

Gazebo Bize Yazdığımız Kodları Gerçek Uçuşdan Önce Kodlarımızı Test Etmeye İmkan Sunuyor Bu Sayede Yazılımsal Sorunlardan Dolayı Çıkabilecek Kazaların Önüne Geçilmiş Olunur

Video : https://youtu.be/v8C3OaFBLzc

```bash
sudo apt-get install python-pip python-dev python3-pip python3-dev
```

```bash
pip install dronekit
```

```bash
pip3 install dronekit
```

- - -

## DroneKit Kullanımı

Video : https://youtu.be/nK-qHtaBpiM

İşte DroneKit Kütüphanesinin Bazı Temel Kodları:

```python
import dronekit
```
DroneKit Kütüphanesini Kodumuzu Dahil Etmek İçin Kullanılır

```python
from dronekit import *
```
DroneKit Kütüphanesinin İçindeki Tüm Paketleri Dahil Etmek İçin Kullanılır

```python
print(drone.armed)
```
Drone'nin Arm Durumunu True Yada False Şekline Verir

```python
drone.armed = True
```
Drone'nin Arm Durumunu True Yada False Şekline Verir

```python
drone = connect("ıp")
```
Bilgisayarın İHA'ya Bağlanmasını Sağlar

```python
drone.mode = VehicleMode("GUIDED")
```
VehicleMode'yi GUIDED Olarak Ayarlanmasına Yarar Yani Bilgisayardan Veri Alabilmesine Bizim Droneye Komut Verebilmemizi Sağlar. Drone 
Stabilize Modundayken Drone Dışarıdan Gelen Verilere Açık Değildir

```python
drone.simple_takeoff(10)
```
Dronenin Kalkış Yapmasını Sağlar Yani Fonksiyona Verdiğimiz Değer Kadar Yükselir

```python
point2 = LocationGlobalRelative(-35.363244, 149.168801, 20)
drone.simple_goto(point2, groundspeed=10)
```
Dronenin poınt2 Olarak Belirtilen Konuma Gitmesini Sağlar

```python
drone.mode = VehicleMode("RTL")
```
Dronenin RTL Moduna Ayarlanmasını Sağlar RTL Kelimesinin Açılımı Olan "Retun To Land" Dronenin Tekrardan Yere Dönmesini Sağlar

- - -

## Temel Kodlar

Daha önce de drone'nin irtifasını ayarlamak için `simple_takeoff` komutunu kullandığımızı söylemsiştim ama bunu koda dökmek gerekise:

```python

from dronekit import connect , VehicleMode , LocationGlobalRelative

drone = connect("127.0.0.1:50000")

drone.mode = VehicleMode("GUIDED")

drone.armed = True

drone.simple_takeoff(20)

```

Bu kodda `from dronekit import connect , VehicleMode , LocationGlobalRelative` satırı dronekit kütüphanesi içerisinden belirlediğimiz paketleri import etmemizi sağlıyor
`drone = connect("127.0.0.1:50000")` Komutu ise drone'ye bağlanmamızı sağlıyor
`drone.mode = VehicleMode("GUIDED")` satırı ile İHA'yı "GUIDED" moduna almamızı sağlıyor
`drone.armed = True` Satırı İHA'yı arm etmemizi sağlıyor
ve son olarak `drone.simple_takeoff(20)` satırı ile Drone'nin yüksekliğini 20 metre olarak ayarlıyoruz
