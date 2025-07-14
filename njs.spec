Summary:	NGS JavaScript Interpreter
Summary(pl.UTF-8):	Interpreter Javascriptu z NGS
Name:		njs
Version:	0.2.5
Release:	1
License:	LGPL
Group:		Development/Languages
Source0:	http://people.ssh.fi/mtr/js/js-%{version}.tar.gz
# Source0-md5:	b299c678e388a170eea09b6e12375152
Patch0:		%{name}-amfix.patch
URL:		http://people.ssh.fi/mtr/js/
# also http://www.bbassett.net/njs/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Requires(post,postun):	/sbin/ldconfig
Conflicts:	js
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The NGS JavaScript is a GPL free interpreter for the JavaScript
language. The JavaScript language is an interpreted C-like language,
developed by Netscape et al.

This implementation is not 100% compatible with the JavaScript
language, found from the Netscape's WWW browsers and servers. To
achieve the following design goals, some shortcuts have been taken in
the implementation, as compared to the Netscape's implementation.

%description -l pl.UTF-8
NGS JavaScript to wolnodostępny interpreter języka JavaScript.
JavaScript jest interpretowanym językiem podobnym do C, rozwijanym
przez Netscape.

Ta implementacja nie jest w 100% zgodna z językiem JavaScript jaki
można znaleźć w przeglądarkach WWW i serwerach Netscape. Aby osiągnąć
zamierzone cele, niezbędne były pewne uproszczenia w porównaniu z
implementacją Netscape.

%package devel
Summary:	Header files for NGS JavaScript library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki NGS JavaScript
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Conflicts:	js-devel

%description devel
Header files for NGS JavaScript library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki NGS JavaScript.

%package static
Summary:	Static NGS JavaScript library
Summary(pl.UTF-8):	Statyczna biblioteka NGS JavaScript
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Conflicts:	js-static

%description static
Static version of NGS JavaScript library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki NGS JavaScript.

%prep
%setup -q -n js-%{version}
%patch -P0 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal} -I am
%{__autoconf}
%{__automake}
%configure \
	--enable-shared \
	--with-pthreads

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_infodir}/js*.info*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
