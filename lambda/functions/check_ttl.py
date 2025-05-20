from aws_xray_sdk.core import xray_recorder
import time
from datetime import datetime

@xray_recorder.capture('handler')
def lambda_handler(event, context):
    """
    Check if a cached timestamp is still valid based on TTL
    
    Parameters:
    - current_time: Current timestamp (ISO 8601 string)
    - cached_timestamp: Timestamp from cached record (ISO 8601 string)
    - ttl_seconds: TTL in seconds (default: 86400 for 24 hours)
    
    Returns:
    {
        "valid": true/false  # Whether the cached timestamp is still valid
    }
    """
    # Parse ISO timestamps to epoch seconds
    def parse_iso_timestamp(ts_string):
        dt = datetime.fromisoformat(ts_string.replace('Z', '+00:00'))
        return dt.timestamp()
    
    # Extract parameters
    current_time_str = event.get('current_time', datetime.utcnow().isoformat())
    cached_timestamp_str = event.get('cached_timestamp', '')
    ttl_seconds = int(event.get('ttl_seconds', 86400))  # Default 24 hours
    
    # Convert ISO timestamps to epoch seconds
    try:
        current_time = parse_iso_timestamp(current_time_str)
        cached_timestamp = parse_iso_timestamp(cached_timestamp_str)
    except Exception as e:
        print(f"Error parsing timestamps: {e}")
        print(f"Current time: {current_time_str}")
        print(f"Cached timestamp: {cached_timestamp_str}")
        # Default to invalid if we can't parse timestamps
        return {
            "valid": False,
            "error": f"Invalid timestamp format: {str(e)}"
        }
    
    # Calculate age of cached timestamp
    time_difference = current_time - cached_timestamp
    
    # Check if timestamp is valid (less than TTL)
    is_valid = time_difference < ttl_seconds
    
    return {
        "valid": is_valid,
        "age_seconds": time_difference,
        "current_time": current_time_str,
        "cached_time": cached_timestamp_str
    } 