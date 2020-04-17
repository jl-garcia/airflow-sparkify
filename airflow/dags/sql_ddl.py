CREATE_STAGE_EVENTS = ("""
        CREATE TABLE IF NOT EXISTS public.staging_events
            (
                artist        varchar(256),
                auth          varchar(256),
                firstname     varchar(256),
                gender        varchar(256),
                iteminsession int4,
                lastname      varchar(256),
                length        numeric(18, 0),
                "level"       varchar(256),
                location      varchar(256),
                "method"      varchar(256),
                page          varchar(256),
                registration  numeric(18, 0),
                sessionid     int4,
                song          varchar(256),
                status        int4,
                ts            int8,
                useragent     varchar(256),
                userid        int4
            );
    """)
