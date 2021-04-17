from owrx.property import PropertyLayer


defaultConfig = PropertyLayer(
    version=7,
    max_clients=20,
    receiver_name="[Callsign]",
    receiver_location="Budapest, Hungary",
    receiver_asl=200,
    receiver_admin="example@example.com",
    receiver_gps=PropertyLayer(lat=47.0, lon=19.0),
    photo_title="Panorama of Budapest from Schönherz Zoltán Dormitory",
    photo_desc="",
    fft_fps=9,
    fft_size=4096,
    fft_voverlap_factor=0.3,
    audio_compression="adpcm",
    fft_compression="adpcm",
    wfm_deemphasis_tau=50e-6,
    digimodes_enable=True,
    digimodes_fft_size=2048,
    digital_voice_unvoiced_quality=1,
    digital_voice_dmr_id_lookup=True,
    sdrs=PropertyLayer(
        rtlsdr=PropertyLayer(
            name="RTL-SDR USB Stick",
            type="rtl_sdr",
            profiles=PropertyLayer(
                **{
                    "70cm": PropertyLayer(
                        name="70cm Repeaters",
                        center_freq=438800000,
                        rf_gain=29,
                        samp_rate=2400000,
                        start_freq=439275000,
                        start_mod="nfm",
                    ),
                    "2m": PropertyLayer(
                        name="2m",
                        center_freq=145000000,
                        rf_gain=29,
                        samp_rate=2048000,
                        start_freq=145725000,
                        start_mod="nfm",
                    ),
                }
            ),
        ),
        airspy=PropertyLayer(
            name="Airspy HF+",
            type="airspyhf",
            rf_gain="auto",
            profiles=PropertyLayer(
                **{
                    "20m": PropertyLayer(
                        name="20m",
                        center_freq=14150000,
                        samp_rate=384000,
                        start_freq=14070000,
                        start_mod="usb",
                    ),
                    "30m": PropertyLayer(
                        name="30m",
                        center_freq=10125000,
                        samp_rate=192000,
                        start_freq=10142000,
                        start_mod="usb",
                    ),
                    "40m": PropertyLayer(
                        name="40m",
                        center_freq=7100000,
                        samp_rate=256000,
                        start_freq=7070000,
                        start_mod="lsb",
                    ),
                    "80m": PropertyLayer(
                        name="80m",
                        center_freq=3650000,
                        samp_rate=384000,
                        start_freq=3570000,
                        start_mod="lsb",
                    ),
                    "49m": PropertyLayer(
                        name="49m Broadcast",
                        center_freq=6050000,
                        samp_rate=384000,
                        start_freq=6070000,
                        start_mod="am",
                    ),
                }
            ),
        ),
        sdrplay=PropertyLayer(
            name="SDRPlay RSP2",
            type="sdrplay",
            antenna="Antenna A",
            profiles=PropertyLayer(
                **{
                    "20m": PropertyLayer(
                        name="20m",
                        center_freq=14150000,
                        rf_gain=0,
                        samp_rate=500000,
                        start_freq=14070000,
                        start_mod="usb",
                    ),
                    "30m": PropertyLayer(
                        name="30m",
                        center_freq=10125000,
                        rf_gain=0,
                        samp_rate=250000,
                        start_freq=10142000,
                        start_mod="usb",
                    ),
                    "40m": PropertyLayer(
                        name="40m",
                        center_freq=7100000,
                        rf_gain=0,
                        samp_rate=500000,
                        start_freq=7070000,
                        start_mod="lsb",
                    ),
                    "80m": PropertyLayer(
                        name="80m",
                        center_freq=3650000,
                        rf_gain=0,
                        samp_rate=500000,
                        start_freq=3570000,
                        start_mod="lsb",
                    ),
                    "49m": PropertyLayer(
                        name="49m Broadcast",
                        center_freq=6000000,
                        rf_gain=0,
                        samp_rate=500000,
                        start_freq=6070000,
                        start_mod="am",
                    ),
                }
            ),
        ),
    ),
    waterfall_scheme="GoogleTurboWaterfall",
    waterfall_levels=PropertyLayer(min=-88, max=-20),
    waterfall_auto_levels=PropertyLayer(min=3, max=10),
    waterfall_auto_min_range=50,
    tuning_precision=2,
    squelch_auto_margin=10,
    google_maps_api_key="",
    map_position_retention_time=2 * 60 * 60,
    decoding_queue_workers=2,
    decoding_queue_length=10,
    wsjt_decoding_depth=3,
    wsjt_decoding_depths=PropertyLayer(jt65=1),
    fst4_enabled_intervals=[15, 30],
    fst4w_enabled_intervals=[120, 300],
    q65_enabled_combinations=["A30", "E120", "C60"],
    js8_enabled_profiles=["normal", "slow"],
    js8_decoding_depth=3,
    services_enabled=False,
    services_decoders=["ft8", "ft4", "wspr", "packet"],
    aprs_callsign="N0CALL",
    aprs_igate_enabled=False,
    aprs_igate_server="euro.aprs2.net",
    aprs_igate_password="",
    aprs_igate_beacon=False,
    aprs_igate_symbol="R&",
    aprs_igate_comment="OpenWebRX APRS gateway",
    # aprs_igate_height=None,
    # aprs_igate_gain=None,
    # aprs_igate_dir=None,
    pskreporter_enabled=False,
    pskreporter_callsign="N0CALL",
    # pskreporter_antenna_information=None,
    wsprnet_enabled=False,
    wsprnet_callsign="N0CALL",
).readonly()
