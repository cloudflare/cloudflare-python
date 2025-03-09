# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["SnapshotGetResponse", "Disk", "Mount", "Netdev", "Thermal"]


class Disk(BaseModel):
    in_progress: float
    """I/Os currently in progress"""

    major: float
    """Device major number"""

    merged: float
    """Reads merged"""

    minor: float
    """Device minor number"""

    name: str
    """Device name"""

    reads: float
    """Reads completed successfully"""

    sectors_read: float
    """Sectors read successfully"""

    sectors_written: float
    """Sectors written successfully"""

    time_in_progress_ms: float
    """Time spent doing I/Os (milliseconds)"""

    time_reading_ms: float
    """Time spent reading (milliseconds)"""

    time_writing_ms: float
    """Time spent writing (milliseconds)"""

    weighted_time_in_progress_ms: float
    """Weighted time spent doing I/Os (milliseconds)"""

    writes: float
    """Writes completed"""

    writes_merged: float
    """Writes merged"""

    connector_id: Optional[str] = None
    """Connector identifier"""

    discards: Optional[float] = None
    """Discards completed successfully"""

    discards_merged: Optional[float] = None
    """Discards merged"""

    flushes: Optional[float] = None
    """Flushes completed successfully"""

    sectors_discarded: Optional[float] = None
    """Sectors discarded"""

    time_discarding_ms: Optional[float] = None
    """Time spent discarding (milliseconds)"""

    time_flushing_ms: Optional[float] = None
    """Time spent flushing (milliseconds)"""


class Mount(BaseModel):
    file_system: str
    """File system on disk (EXT4, NTFS, etc.)"""

    kind: str
    """Kind of disk (HDD, SSD, etc.)"""

    mount_point: str
    """Path where disk is mounted"""

    name: str
    """Name of the disk mount"""

    available_bytes: Optional[float] = None
    """Available disk size (bytes)"""

    connector_id: Optional[str] = None
    """Connector identifier"""

    is_read_only: Optional[bool] = None
    """Determines whether the disk is read-only"""

    is_removable: Optional[bool] = None
    """Determines whether the disk is removable"""

    total_bytes: Optional[float] = None
    """Total disk size (bytes)"""


class Netdev(BaseModel):
    name: str
    """Name of the network device"""

    recv_bytes: float
    """Total bytes received"""

    recv_compressed: float
    """Compressed packets received"""

    recv_drop: float
    """Packets dropped"""

    recv_errs: float
    """Bad packets received"""

    recv_fifo: float
    """FIFO overruns"""

    recv_frame: float
    """Frame alignment errors"""

    recv_multicast: float
    """Multicast packets received"""

    recv_packets: float
    """Total packets received"""

    sent_bytes: float
    """Total bytes transmitted"""

    sent_carrier: float
    """Number of packets not sent due to carrier errors"""

    sent_colls: float
    """Number of collisions"""

    sent_compressed: float
    """Number of compressed packets transmitted"""

    sent_drop: float
    """Number of packets dropped during transmission"""

    sent_errs: float
    """Number of transmission errors"""

    sent_fifo: float
    """FIFO overruns"""

    sent_packets: float
    """Total packets transmitted"""

    connector_id: Optional[str] = None
    """Connector identifier"""


class Thermal(BaseModel):
    label: str
    """Sensor identifier for the component"""

    connector_id: Optional[str] = None
    """Connector identifier"""

    critical_celcius: Optional[float] = None
    """Critical failure temperature of the component (degrees Celsius)"""

    current_celcius: Optional[float] = None
    """Current temperature of the component (degrees Celsius)"""

    max_celcius: Optional[float] = None
    """Maximum temperature of the component (degrees Celsius)"""


class SnapshotGetResponse(BaseModel):
    count_reclaim_failures: float
    """Count of failures to reclaim space"""

    count_reclaimed_paths: float
    """Count of reclaimed paths"""

    count_record_failed: float
    """Count of failed snapshot recordings"""

    count_transmit_failures: float
    """Count of failed snapshot transmissions"""

    t: float
    """Time the Snapshot was recorded (seconds since the Unix epoch)"""

    v: str
    """Version"""

    cpu_count: Optional[float] = None
    """Count of processors/cores"""

    cpu_pressure_10s: Optional[float] = None
    """Percentage of time over a 10 second window that tasks were stalled"""

    cpu_pressure_300s: Optional[float] = None
    """Percentage of time over a 5 minute window that tasks were stalled"""

    cpu_pressure_60s: Optional[float] = None
    """Percentage of time over a 1 minute window that tasks were stalled"""

    cpu_pressure_total_us: Optional[float] = None
    """Total stall time (microseconds)"""

    cpu_time_guest_ms: Optional[float] = None
    """Time spent running a virtual CPU or guest OS (milliseconds)"""

    cpu_time_guest_nice_ms: Optional[float] = None
    """Time spent running a niced guest (milliseconds)"""

    cpu_time_idle_ms: Optional[float] = None
    """Time spent in idle state (milliseconds)"""

    cpu_time_iowait_ms: Optional[float] = None
    """Time spent wait for I/O to complete (milliseconds)"""

    cpu_time_irq_ms: Optional[float] = None
    """Time spent servicing interrupts (milliseconds)"""

    cpu_time_nice_ms: Optional[float] = None
    """Time spent in low-priority user mode (milliseconds)"""

    cpu_time_softirq_ms: Optional[float] = None
    """Time spent servicing softirqs (milliseconds)"""

    cpu_time_steal_ms: Optional[float] = None
    """Time stolen (milliseconds)"""

    cpu_time_system_ms: Optional[float] = None
    """Time spent in system mode (milliseconds)"""

    cpu_time_user_ms: Optional[float] = None
    """Time spent in user mode (milliseconds)"""

    disks: Optional[List[Disk]] = None

    ha_state: Optional[str] = None
    """Name of high availability state"""

    ha_value: Optional[float] = None
    """
    Numeric value associated with high availability state (0 = unknown, 1 = active,
    2 = standby, 3 = disabled, 4 = fault)
    """

    io_pressure_full_10s: Optional[float] = None
    """Percentage of time over a 10 second window that all tasks were stalled"""

    io_pressure_full_300s: Optional[float] = None
    """Percentage of time over a 5 minute window that all tasks were stalled"""

    io_pressure_full_60s: Optional[float] = None
    """Percentage of time over a 1 minute window that all tasks were stalled"""

    io_pressure_full_total_us: Optional[float] = None
    """Total stall time (microseconds)"""

    io_pressure_some_10s: Optional[float] = None
    """Percentage of time over a 10 second window that some tasks were stalled"""

    io_pressure_some_300s: Optional[float] = None
    """Percentage of time over a 3 minute window that some tasks were stalled"""

    io_pressure_some_60s: Optional[float] = None
    """Percentage of time over a 1 minute window that some tasks were stalled"""

    io_pressure_some_total_us: Optional[float] = None
    """Total stall time (microseconds)"""

    kernel_btime: Optional[float] = None
    """Boot time (seconds since Unix epoch)"""

    kernel_ctxt: Optional[float] = None
    """Number of context switches that the system underwent"""

    kernel_processes: Optional[float] = None
    """Number of forks since boot"""

    kernel_processes_blocked: Optional[float] = None
    """Number of processes blocked waiting for I/O"""

    kernel_processes_running: Optional[float] = None
    """Number of processes in runnable state"""

    load_average_15m: Optional[float] = None
    """The fifteen-minute load average"""

    load_average_1m: Optional[float] = None
    """The one-minute load average"""

    load_average_5m: Optional[float] = None
    """The five-minute load average"""

    load_average_cur: Optional[float] = None
    """Number of currently runnable kernel scheduling entities"""

    load_average_max: Optional[float] = None
    """Number of kernel scheduling entities that currently exist on the system"""

    memory_active_bytes: Optional[float] = None
    """Memory that has been used more recently"""

    memory_anon_hugepages_bytes: Optional[float] = None
    """Non-file backed huge pages mapped into user-space page tables"""

    memory_anon_pages_bytes: Optional[float] = None
    """Non-file backed pages mapped into user-space page tables"""

    memory_available_bytes: Optional[float] = None
    """Estimate of how much memory is available for starting new applications"""

    memory_bounce_bytes: Optional[float] = None
    """Memory used for block device bounce buffers"""

    memory_buffers_bytes: Optional[float] = None
    """Relatively temporary storage for raw disk blocks"""

    memory_cached_bytes: Optional[float] = None
    """In-memory cache for files read from the disk"""

    memory_cma_free_bytes: Optional[float] = None
    """Free CMA (Contiguous Memory Allocator) pages"""

    memory_cma_total_bytes: Optional[float] = None
    """Total CMA (Contiguous Memory Allocator) pages"""

    memory_commit_limit_bytes: Optional[float] = None
    """Total amount of memory currently available to be allocated on the system"""

    memory_committed_as_bytes: Optional[float] = None
    """Amount of memory presently allocated on the system"""

    memory_dirty_bytes: Optional[float] = None
    """Memory which is waiting to get written back to the disk"""

    memory_free_bytes: Optional[float] = None
    """The sum of LowFree and HighFree"""

    memory_high_free_bytes: Optional[float] = None
    """Amount of free highmem"""

    memory_high_total_bytes: Optional[float] = None
    """Total amount of highmem"""

    memory_hugepages_free: Optional[float] = None
    """The number of huge pages in the pool that are not yet allocated"""

    memory_hugepages_rsvd: Optional[float] = None
    """
    Number of huge pages for which a commitment has been made, but no allocation has
    yet been made
    """

    memory_hugepages_surp: Optional[float] = None
    """Number of huge pages in the pool above the threshold"""

    memory_hugepages_total: Optional[float] = None
    """The size of the pool of huge pages"""

    memory_hugepagesize_bytes: Optional[float] = None
    """The size of huge pages"""

    memory_inactive_bytes: Optional[float] = None
    """Memory which has been less recently used"""

    memory_k_reclaimable_bytes: Optional[float] = None
    """
    Kernel allocations that the kernel will attempt to reclaim under memory pressure
    """

    memory_kernel_stack_bytes: Optional[float] = None
    """Amount of memory allocated to kernel stacks"""

    memory_low_free_bytes: Optional[float] = None
    """Amount of free lowmem"""

    memory_low_total_bytes: Optional[float] = None
    """Total amount of lowmem"""

    memory_mapped_bytes: Optional[float] = None
    """Files which have been mapped into memory"""

    memory_page_tables_bytes: Optional[float] = None
    """Amount of memory dedicated to the lowest level of page tables"""

    memory_per_cpu_bytes: Optional[float] = None
    """Memory allocated to the per-cpu alloctor used to back per-cpu allocations"""

    memory_pressure_full_10s: Optional[float] = None
    """Percentage of time over a 10 second window that all tasks were stalled"""

    memory_pressure_full_300s: Optional[float] = None
    """Percentage of time over a 5 minute window that all tasks were stalled"""

    memory_pressure_full_60s: Optional[float] = None
    """Percentage of time over a 1 minute window that all tasks were stalled"""

    memory_pressure_full_total_us: Optional[float] = None
    """Total stall time (microseconds)"""

    memory_pressure_some_10s: Optional[float] = None
    """Percentage of time over a 10 second window that some tasks were stalled"""

    memory_pressure_some_300s: Optional[float] = None
    """Percentage of time over a 5 minute window that some tasks were stalled"""

    memory_pressure_some_60s: Optional[float] = None
    """Percentage of time over a 1 minute window that some tasks were stalled"""

    memory_pressure_some_total_us: Optional[float] = None
    """Total stall time (microseconds)"""

    memory_s_reclaimable_bytes: Optional[float] = None
    """Part of slab that can be reclaimed on memory pressure"""

    memory_s_unreclaim_bytes: Optional[float] = None
    """Part of slab that cannot be reclaimed on memory pressure"""

    memory_secondary_page_tables_bytes: Optional[float] = None
    """Amount of memory dedicated to the lowest level of page tables"""

    memory_shmem_bytes: Optional[float] = None
    """Amount of memory consumed by tmpfs"""

    memory_shmem_hugepages_bytes: Optional[float] = None
    """Memory used by shmem and tmpfs, allocated with huge pages"""

    memory_shmem_pmd_mapped_bytes: Optional[float] = None
    """Shared memory mapped into user space with huge pages"""

    memory_slab_bytes: Optional[float] = None
    """In-kernel data structures cache"""

    memory_swap_cached_bytes: Optional[float] = None
    """Memory swapped out and back in while still in swap file"""

    memory_swap_free_bytes: Optional[float] = None
    """Amount of swap space that is currently unused"""

    memory_swap_total_bytes: Optional[float] = None
    """Total amount of swap space available"""

    memory_total_bytes: Optional[float] = None
    """Total usable RAM"""

    memory_vmalloc_chunk_bytes: Optional[float] = None
    """Largest contiguous block of vmalloc area which is free"""

    memory_vmalloc_total_bytes: Optional[float] = None
    """Total size of vmalloc memory area"""

    memory_vmalloc_used_bytes: Optional[float] = None
    """Amount of vmalloc area which is used"""

    memory_writeback_bytes: Optional[float] = None
    """Memory which is actively being written back to the disk"""

    memory_writeback_tmp_bytes: Optional[float] = None
    """Memory used by FUSE for temporary writeback buffers"""

    memory_z_swap_bytes: Optional[float] = None
    """Memory consumed by the zswap backend, compressed"""

    memory_z_swapped_bytes: Optional[float] = None
    """Amount of anonymous memory stored in zswap, uncompressed"""

    mounts: Optional[List[Mount]] = None

    netdevs: Optional[List[Netdev]] = None

    snmp_icmp_in_addr_mask_reps: Optional[float] = None
    """Number of ICMP Address Mask Reply messages received"""

    snmp_icmp_in_addr_masks: Optional[float] = None
    """Number of ICMP Address Mask Request messages received"""

    snmp_icmp_in_csum_errors: Optional[float] = None
    """Number of ICMP messages received with bad checksums"""

    snmp_icmp_in_dest_unreachs: Optional[float] = None
    """Number of ICMP Destination Unreachable messages received"""

    snmp_icmp_in_echo_reps: Optional[float] = None
    """Number of ICMP Echo Reply messages received"""

    snmp_icmp_in_echos: Optional[float] = None
    """Number of ICMP Echo (request) messages received"""

    snmp_icmp_in_errors: Optional[float] = None
    """Number of ICMP messages received with ICMP-specific errors"""

    snmp_icmp_in_msgs: Optional[float] = None
    """Number of ICMP messages received"""

    snmp_icmp_in_parm_probs: Optional[float] = None
    """Number of ICMP Parameter Problem messages received"""

    snmp_icmp_in_redirects: Optional[float] = None
    """Number of ICMP Redirect messages received"""

    snmp_icmp_in_src_quenchs: Optional[float] = None
    """Number of ICMP Source Quench messages received"""

    snmp_icmp_in_time_excds: Optional[float] = None
    """Number of ICMP Time Exceeded messages received"""

    snmp_icmp_in_timestamp_reps: Optional[float] = None
    """Number of ICMP Address Mask Request messages received"""

    snmp_icmp_in_timestamps: Optional[float] = None
    """Number of ICMP Timestamp (request) messages received"""

    snmp_icmp_out_addr_mask_reps: Optional[float] = None
    """Number of ICMP Address Mask Reply messages sent"""

    snmp_icmp_out_addr_masks: Optional[float] = None
    """Number of ICMP Address Mask Request messages sent"""

    snmp_icmp_out_dest_unreachs: Optional[float] = None
    """Number of ICMP Destination Unreachable messages sent"""

    snmp_icmp_out_echo_reps: Optional[float] = None
    """Number of ICMP Echo Reply messages sent"""

    snmp_icmp_out_echos: Optional[float] = None
    """Number of ICMP Echo (request) messages sent"""

    snmp_icmp_out_errors: Optional[float] = None
    """
    Number of ICMP messages which this entity did not send due to ICMP-specific
    errors
    """

    snmp_icmp_out_msgs: Optional[float] = None
    """Number of ICMP messages attempted to send"""

    snmp_icmp_out_parm_probs: Optional[float] = None
    """Number of ICMP Parameter Problem messages sent"""

    snmp_icmp_out_redirects: Optional[float] = None
    """Number of ICMP Redirect messages sent"""

    snmp_icmp_out_src_quenchs: Optional[float] = None
    """Number of ICMP Source Quench messages sent"""

    snmp_icmp_out_time_excds: Optional[float] = None
    """Number of ICMP Time Exceeded messages sent"""

    snmp_icmp_out_timestamp_reps: Optional[float] = None
    """Number of ICMP Timestamp Reply messages sent"""

    snmp_icmp_out_timestamps: Optional[float] = None
    """Number of ICMP Timestamp (request) messages sent"""

    snmp_ip_default_ttl: Optional[float] = None
    """Default value of the Time-To-Live field of the IP header"""

    snmp_ip_forw_datagrams: Optional[float] = None
    """Number of datagrams forwarded to their final destination"""

    snmp_ip_forwarding_enabled: Optional[bool] = None
    """Set when acting as an IP gateway"""

    snmp_ip_frag_creates: Optional[float] = None
    """Number of datagrams generated by fragmentation"""

    snmp_ip_frag_fails: Optional[float] = None
    """Number of datagrams discarded because fragmentation failed"""

    snmp_ip_frag_oks: Optional[float] = None
    """Number of datagrams successfully fragmented"""

    snmp_ip_in_addr_errors: Optional[float] = None
    """Number of input datagrams discarded due to errors in the IP address"""

    snmp_ip_in_delivers: Optional[float] = None
    """Number of input datagrams successfully delivered to IP user-protocols"""

    snmp_ip_in_discards: Optional[float] = None
    """Number of input datagrams otherwise discarded"""

    snmp_ip_in_hdr_errors: Optional[float] = None
    """Number of input datagrams discarded due to errors in the IP header"""

    snmp_ip_in_receives: Optional[float] = None
    """Number of input datagrams received from interfaces"""

    snmp_ip_in_unknown_protos: Optional[float] = None
    """Number of input datagrams discarded due unknown or unsupported protocol"""

    snmp_ip_out_discards: Optional[float] = None
    """Number of output datagrams otherwise discarded"""

    snmp_ip_out_no_routes: Optional[float] = None
    """Number of output datagrams discarded because no route matched"""

    snmp_ip_out_requests: Optional[float] = None
    """Number of datagrams supplied for transmission"""

    snmp_ip_reasm_fails: Optional[float] = None
    """Number of failures detected by the reassembly algorithm"""

    snmp_ip_reasm_oks: Optional[float] = None
    """Number of datagrams successfully reassembled"""

    snmp_ip_reasm_reqds: Optional[float] = None
    """Number of fragments received which needed to be reassembled"""

    snmp_ip_reasm_timeout: Optional[float] = None
    """Number of seconds fragments are held while awaiting reassembly"""

    snmp_tcp_active_opens: Optional[float] = None
    """Number of times TCP transitions to SYN-SENT from CLOSED"""

    snmp_tcp_attempt_fails: Optional[float] = None
    """
    Number of times TCP transitions to CLOSED from SYN-SENT or SYN-RCVD, plus
    transitions to LISTEN from SYN-RCVD
    """

    snmp_tcp_curr_estab: Optional[float] = None
    """Number of TCP connections in ESTABLISHED or CLOSE-WAIT"""

    snmp_tcp_estab_resets: Optional[float] = None
    """Number of times TCP transitions to CLOSED from ESTABLISHED or CLOSE-WAIT"""

    snmp_tcp_in_csum_errors: Optional[float] = None
    """Number of TCP segments received with checksum errors"""

    snmp_tcp_in_errs: Optional[float] = None
    """Number of TCP segments received in error"""

    snmp_tcp_in_segs: Optional[float] = None
    """Number of TCP segments received"""

    snmp_tcp_max_conn: Optional[float] = None
    """Limit on the total number of TCP connections"""

    snmp_tcp_out_rsts: Optional[float] = None
    """Number of TCP segments sent with RST flag"""

    snmp_tcp_out_segs: Optional[float] = None
    """Number of TCP segments sent"""

    snmp_tcp_passive_opens: Optional[float] = None
    """Number of times TCP transitions to SYN-RCVD from LISTEN"""

    snmp_tcp_retrans_segs: Optional[float] = None
    """Number of TCP segments retransmitted"""

    snmp_tcp_rto_max: Optional[float] = None
    """
    Maximum value permitted by a TCP implementation for the retransmission timeout
    (milliseconds)
    """

    snmp_tcp_rto_min: Optional[float] = None
    """
    Minimum value permitted by a TCP implementation for the retransmission timeout
    (milliseconds)
    """

    snmp_udp_in_datagrams: Optional[float] = None
    """Number of UDP datagrams delivered to UDP applications"""

    snmp_udp_in_errors: Optional[float] = None
    """
    Number of UDP datagrams failed to be delivered for reasons other than lack of
    application at the destination port
    """

    snmp_udp_no_ports: Optional[float] = None
    """
    Number of UDP datagrams received for which there was not application at the
    destination port
    """

    snmp_udp_out_datagrams: Optional[float] = None
    """Number of UDP datagrams sent"""

    system_boot_time_s: Optional[float] = None
    """Boottime of the system (seconds since the Unix epoch)"""

    thermals: Optional[List[Thermal]] = None

    uptime_idle_ms: Optional[float] = None
    """Sum of how much time each core has spent idle"""

    uptime_total_ms: Optional[float] = None
    """Uptime of the system, including time spent in suspend"""
