import subprocess
import json

class StatsCollector:
    def collect(self, device):
        result = subprocess.run(["lvs", 
            "--reportformat", "json", 
            "--noheadings", 
            "-o", "cache_read_hits,cache_read_misses,cache_write_hits,cache_write_misses,cache_dirty_blocks", 
            device], 
            capture_output=True, 
            check=True)

        json_result = json.loads(result.stdout.decode('UTF-8'))

        return json_result['report'][0]['lv'][0]

