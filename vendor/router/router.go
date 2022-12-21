package router

import (
	"api"
	"net/http"

	// "v1/vendor/api"

	"views"
)

// 配置路由与函数之间的映射关系
func Router() {
	// //1. 页面  views 2. api 数据（json） 3. 静态资源
	// http.Handle("/", contexts.Context)
	// //http://localhost:8080/c/1  1参数 分类的id
	// contexts.Context.Handler("/c/{id}", views.HTML.CategoryNew)
	// contexts.Context.Handler("/login", views.HTML.LoginNew)
	// 主页
	http.HandleFunc("/", views.HTML.Index)
	//http://localhost:8080/c/1  1参数 分类的id
	// 根据页码分页查询
	http.HandleFunc("/c/", views.HTML.Category)
	// 登录页面
	http.HandleFunc("/login", views.HTML.Login)
	//http://localhost:8080/p/7.html
	// 博客详情（根据博客id将博客查询出来）
	http.HandleFunc("/p/", views.HTML.Detail)
	// 写博客（收集到博客信息之后向接口发送信息）
	http.HandleFunc("/writing", views.HTML.Writing)
	// 归档页面
	http.HandleFunc("/pigeonhole", views.HTML.Pigeonhole)

	// -----------------------后端接口(处理数据)--------------------------//
	http.HandleFunc("/api/v1/post", api.API.SaveAndUpdatePost)
	http.HandleFunc("/api/v1/post/", api.API.GetPost)
	http.HandleFunc("/api/v1/post/search", api.API.SearchPost)
	http.HandleFunc("/api/v1/qiniu/token", api.API.QiniuToken)
	http.HandleFunc("/api/v1/login", api.API.Login)

	//-------------------------静态资源的映射配置---------------------------//
	http.Handle("/resource/", http.StripPrefix("/resource/", http.FileServer(http.Dir("public/resource/"))))
}
