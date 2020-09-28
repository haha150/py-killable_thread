from threading import Thread


class KillableThread(Thread):
    def get_id(self):
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for tid, thread in threading._active.items():
            if thread is self:
                return tid
   
    def kill(self):
        thread_id = self.get_id()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread_id), ctypes.py_object(SystemExit))
        if res == 0:
            raise ValueError("invalid thread id")
        elif res != 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread_id), None)
            raise SystemError("PyThreadState_SetAsyncExc failed")
