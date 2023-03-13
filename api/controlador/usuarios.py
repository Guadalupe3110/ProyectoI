from flask import Flask, render_template, request, send_from_directory, redirect, url_for, session
from modelo.db_usuarios import CL_UsuarioDB


class CL_Usuario:
    
    def FN_Usuario(self):
        token = request.headers.get('token')
        if (token == "7ca057fab5edfb90831da61d0c3cc5bd"):
            contenido = request.get_json(force = True)
            respuesta = {"Usuario": contenido}
            respuesta = CL_UsuarioDB().FN_NuevoUsuario(respuesta)#Insertar usuario en base de datos 
            if(len(respuesta) != 0):
                res = "200 OK: Usuario creado con exito"
            else:
                res = "Error 400"
            return res
        else:
            return "Token invalido"
        
    def FN_ModificarToken(self, usuario):
        return CL_UsuarioDB().FN_ModificarUsuario(usuario)
