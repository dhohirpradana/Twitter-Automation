from ctypes import cdll

main = cdll.LoadLibrary("app.so")

main()
