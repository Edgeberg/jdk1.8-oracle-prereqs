Dummy package to provide some /bin/* RPM prerequisites that aren't actually
provided by any Red Hat RPM-based Linux distros, to make the Oracle JRE/JDK 1.8
RPMs that can be downloaded from Oracle's OTN site happy.

The coreutils RPM package currently includes "Provides:" for some but not all of
the /bin/* files it delivers (true for RHEL/CentOS 7, 8 and 9 that I know of,
as well as Fedora versions at least including 31 through 33). However, it does
not appear as though providing these "Provides" is "Required" by anything other
than niche packages such as Oracle's Java RPMs, so my vote would be that Oracle
changes its packaging rather than Red Hat adding these itself.

Without fudging the dependencies in this way, the main alternative is to bypass
yum/dnf and use rpm -i jdk1.8[...].rpm.

Note that this package does not actually contain any files for the filesystem.
