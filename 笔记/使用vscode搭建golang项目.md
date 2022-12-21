## 前言

VC code是一款巨好用的编辑器，使用vs code开发项目需要进行一些配置。

因为项目中需要用到很多的包，无论是自己建的还是第三方的。

由于go语言的生态环境没有java与python那样好，没有一个好的的包管理工具这给想用vs code开发golang项目的同学带来了困扰

接下来就带大家了解一下如何在没有集成开发环境下手刃一个go语言项目

## 安装go语言环境

这个巨简单就不说了

## 了解Go开发相关的环境变量

````properties
#GOROOT：GOROOT就是Go的安装目录，（类似于java的JDK）。不用往环境变量配置。包管理方式变成Go Module之后就用处不大了。
GOROOT = D:\Go (你安装go环境的目录)   
#GOPATH：GOPATH是我们的工作空间，保存go项目代码和第三方依赖包。安装后，在环境变量中有。
GOPATH = %USERPROFILE%\go
#配置代理加速（因为go语言用到的包大多数都在github）
GOPROXY=https://goproxy.cn,direct

````

## 熟悉Go Module

- (1)使用 go module 管理依赖后会在项目根目录下生成两个文件 go.mod 和 go.sum。go.mod 中会记录当前项目的所依赖的包的信息。

- (2)在需要使用时才开启GO111MODULE = on，平时GO111MODULE = off，避免在已有项目中意外引入 go module。

- (3)**go module 的目的是依赖管理，所以使用 go module 时你**可以舍弃 go get 命令**(但是不是禁止使用, 如果要指定包的版本或更新包可使用go get，平时没有必要使用)

````
要使用go module 首先要设置GO111MODULE=on，GO111MODULE 有三个值，off、on、auto。auto 会根据当前目录下是否有 go.mod 文件来判断是否使用 modules 功能。平时 GO111MODULE = off，在需要使用的时候再开启，避免在已有项目中意外引入 go module。
set GO111MODULE=on
go env // 查看 GO111MODULE 选项为 on 代表修改成功
````

````properties
#初始化。先进入test项目下，然后执行此命令，项目根目录会出现一个 go.mod 文件
go mod init test 
#检测依赖。tidy会检测该文件夹目录下所有引入的依赖，写入 go.mod 文件，写入后你会发现 go.mod 文件有所变动
go mod tidy 
#下载依赖。我们需要将依赖下载至本地，而不是使用 go get
go mod download 
#导入依赖。此命令会将刚才下载至 GOPATH 下的依赖转移至该项目根目录下的 vendor(自动新建) 文件夹下, 此时我们就可以使用这些依赖了
go mod vendor 
#依赖更新：这里的更新不是指版本的更新，而是指引入新依赖，依赖更新请从检测依赖部分一直执行即可：
go mod tidy
go mod download
go mod vendor

注：go mod vendor创建的文件夹里面可以放用户自己的定制的包（放入后直接用包名就可以导入项目不需要相对路径）
````

## 创建一个go项目

1. 新建文件夹demo，作为项目根目录
2. cmd，执行命令：go mod init demo 此时会生成一个go.mod文件(存放项目依赖)
3. vscode打开文件：选择项目根目录demo
4. 新建main.go文件：在根目录下创建main.go文件
5. 执行
   1. go mod tidy        // 添加或者删除 modules，取决于依赖的引用 （执行完生成go.sum文件）
   2. go mod vendor      // 复制依赖到 vendor 目录下

如图

![image-20221105191644534](C:\Users\123\AppData\Roaming\Typora\typora-user-images\image-20221105191644534.png)

![image-20221105191707488](C:\Users\123\AppData\Roaming\Typora\typora-user-images\image-20221105191707488.png)



此时就可以放肆地开发了。