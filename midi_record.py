import os, signal, time, pytz, sys
from datetime import datetime
from subprocess import check_output, Popen



recpath = '/home/pi/projects/midi_recorder/log'
tz = pytz.timezone('Europe/Stockholm')
arec = '/usr/bin/arecordmidi'


def get_ports():
        output = check_output([arec, '-l'], universal_newlines=True)
        res = [line.split()[0] for line in output.split('\n') if 'MIDI' in line]
        return res



def get_pids(proc):
        try:
                output = check_output(['pgrep', proc], universal_newlines=True)
                return [int(pid) for pid in output.split()]
        except: return []



def arec_start_record():
        ports = get_ports()

        if ports:
            timestr = datetime.now(tz).strftime('%Y-%m-%d_%H.%M.%S')
            cmd = [arec, '-p', ports[0], '%s/rec%s.mid' % (recpath, timestr)]
            pid = Popen(cmd).pid
            print('Started [%d] %s' % (pid, ' '.join(cmd)))

def arec_stop_record():
        pids = get_pids('arecordmidi')

        if pids:
            pids = get_pids('arecordmidi')
            os.kill(pids[0], signal.SIGINT)
            print('Killed (SIGINT) [%d]' % pids[0])
