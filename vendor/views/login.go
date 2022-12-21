package views

import (
	"common"
	"config"
	"contexts"
	"net/http"
)

func (*HTMLApi) LoginNew(ctx *contexts.MsContext) {
	login := common.Template.Login

	login.WriteData(ctx.W, config.Cfg.Viewer)
}
func (*HTMLApi) Login(w http.ResponseWriter, r *http.Request) {
	login := common.Template.Login

	login.WriteData(w, config.Cfg.Viewer)
}
