from ReadWriteMemory import ReadWriteMemory, ReadWriteMemoryError

DEBUG = False

# marker in openGOAL memory to search for
MARKER_BYTES = b'UnLiStEdStRaTs_JaK1\x00'

class OpenGoalAutoTracker(object):

  def connect_and_find_markers(self, close_process: bool) -> bool:
    # find marker in process memory
    self.process.open()

    # try any previously saved marker_addr
    if self.marker_addr is not None:
      # verify
      tmp_bytes = self.process.readByte(self.marker_addr, 20)
        
      if tmp_bytes == MARKER_BYTES:
        # keep marker_addr
        if DEBUG:
          print(f'found marker at address: {tmp}')
      else:
        # erase marker_addr
        self.marker_addr = None

    # no saved+verified marker_addr, need to search
    if self.marker_addr is None:
      # only need to search through first module
      modules = self.process.get_modules()
      mem_start = modules[0]
      mem_end = modules[1]

      tmp = mem_start
      while tmp < mem_end:
        # save some time by checking only first byte initially
        first_byte = self.process.readByte(tmp, 1)

        if first_byte == b'U':
          # first byte matched, check the full 20 bytes
          tmp_bytes = self.process.readByte(tmp, 20)
          
          if tmp_bytes == MARKER_BYTES:
            if DEBUG:
              print(f'found marker at address: {tmp}')
            break
        
        # start from next byte
        tmp += 1

      if tmp < mem_end:
        self.marker_addr = tmp

    # if still not marker_addr, something went wrong
    if self.marker_addr is None:
      print(f'Couldn''t find base address for {MARKER_BYTES}!')
      return False

    # The address of the GOAL struct is stored in a u64 next to the marker!
    # 20 bytes for "UnLiStEdStRaTs_JaK1 " | 4 bytes padding | 8 bytes (u64) for GOAL struct address
    #   so GOAL struct address is 24 = 0x18 bytes from base_ptr
    goal_struct_addr_ptr = self.marker_addr + 24
    self.goal_struct_addr = int.from_bytes(self.process.readByte(goal_struct_addr_ptr, 8), byteorder='little', signed=False)
    if DEBUG:
      print(f'found goal_struct_addr as: {self.goal_struct_addr}')

    if close_process:
      self.process.close()

    return True

  def __init__(self):
    try:
      self.process = ReadWriteMemory().get_process_by_name('gk')
    except ReadWriteMemoryError as e:
      print(f'Error finding process gk.exe: {e}')
      exit(1)
    
    self.marker_addr = None

    if not self.connect_and_find_markers(True):
      print(f'Error finding markers in memory')
      exit(2)

  def read_field_values(self, fields):
    if not self.connect_and_find_markers(False):
      print(f'Error finding markers in memory')
      exit(3)

    field_values = {}
    
    for key in fields:
      if fields[key]["icon_type"] == "skip":
        continue

      field_values[key] = int.from_bytes(self.process.readByte(self.goal_struct_addr + fields[key]["offset"], fields[key]["length"]), byteorder='little', signed=False)

    if DEBUG:
      print(f'field_values: {field_values}')

    self.process.close()

    return field_values