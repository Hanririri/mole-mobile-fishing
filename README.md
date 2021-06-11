# mole-mobile-fishing
For auto fishing in mole mobile game.<br/>
摩尔庄园手游钓鱼这种事情简单机械重复，枯燥乏味，为什么不让计算机替代人类完成这样的工作呢？<br/>

## How to use
在电脑上运行安卓模拟器运行摩尔庄园。先走到钓鱼的地方，试着钓鱼确定鱼竿落点，然后命令行运行本程序。<br/>
程序一开始需要框选识别的范围，有两个范围要识别，分别是头顶的感叹号和鱼竿落点附近的浅蓝色圆圈。<br/>
识别的过程请不要放竿钓鱼。识别完成后把鼠标移动到钓鱼按钮，程序自动实现鼠标左键点按功能，一直执行钓鱼。<br/>
注：可能需要管理员权限。

## How it works
运行的时候先框选一个区域，然后程序在一个while死循环里不断判断所框选的区域颜色是否发生变化来判断是否收杆。<br/>
摩尔庄园里的钓鱼虽然有了一个绿圈的设定，但发现延时2s鱼在绿圈里的概率有九成。所以通过判断人物头上是否出现感叹号来钓鱼，并且等待2s收杆，然后延时，左键，延时，左键。<br/>
为了判断是否在钓鱼状态，增加了一个判别位置，鱼竿下水了那一部分是浅蓝色的，也是框选该区域然后判断颜色是否发生变化来判断在不在钓鱼状态，不在钓鱼状态就左键抛杆。<br/>
![Image](https://github.com/Hanririri/mole-mobile-fishing/blob/main/pic1.png)<br/>
![Image](https://github.com/Hanririri/mole-mobile-fishing/blob/main/pic2.png)<br/>

## Thanks
kirb3<br/>
https://github.com/kirb3/minecraft-fisher
