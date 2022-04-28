Name:           jdk1.8-oracle-prereqs
Version:        1.0
Release:        1%{?dist}
Summary:        "Provides" /bin/* prereqs for Oracle's Java 8 RPMs.
BuildArch:      noarch
Group:          System Environment/Base
License:        Public Domain
URL:            https://github.com/Edgeberg/jdk1.8-oracle-prereqs

Provides: /bin/basename
Provides: /bin/cp
Provides: /bin/ls
Provides: /bin/mkdir
Provides: /bin/mv
Provides: /bin/pwd
Provides: /bin/sort

%description
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

%prep


%build


%install
#rm -rf $RPM_BUILD_ROOT


%files


%changelog
* Thu Apr 28 2022 Edgeberg <Edgeberg@outlook.com.au> 1.0-1
- Initial spec based on the output of "dnf localinstall jdk-8u331-linux-x64.rpm"
