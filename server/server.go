package server

import (
	"fmt"
	"log"
	"net/http"
	"router"
)

var App = &MsServer{}

type MsServer struct {
}

func (*MsServer) Start(ip, port string) {
	// 定义网络服务对象
	fmt.Println(port)
	server := &http.Server{
		Addr: port,
	}
	//路由映射
	router.Router()
	// 开启监听
	if err := server.ListenAndServe(); err != nil {
		log.Println(err)
	}
}
