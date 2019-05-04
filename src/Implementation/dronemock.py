#!/usr/bin/env python

import numpy as np

class Fake_frame_read:
    """Mimic the tello frame interface. Loops the video when finished."""
    
    def __init__(self, path):
        self.full = np.load(path)
        #self._frame = myframe(self.full)     
        self.i = -1
        
    def _load_frame(self):
        # Using a generator was too convoluted.
        self.i += 1
        nframes = len(self.full)
        
        if self.i == len(self.full):
            print('Cycle movie...')
            self.i = 0
                
        return self.full[self.i]
        
    frame = property(fget=_load_frame)   