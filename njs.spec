Summary:	NGS JavaScript Interpreter
Summary(pl):	Interpreter Javascriptu z NGS
Name:		njs
Version:	0.2.5
Release:	1
License:	LGPL
Group:		Development/Languages
Source0:	http://people.ssh.fi/mtr/js/js-%{version}.tar.gz
Patch0:		%{name}-amfix.patch
URL:		http://people.ssh.fi/mtr/js/
# also http://www.bbassett.net/njs/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Requires(post,postun):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The NGS JavaScript is a GPL free interpreter for the JavaScript
language. The JavaScript language is an interpreted C-like language,
developed by Netscape et al.

This implementation is not 100% compatible with the JavaScript
language, found from the Netscape's WWW browsers and servers. To
achieve the following design goals, some shortcuts have been taken in
the implementation, as compared to the Netscape's implementation.

%description -l pl
NGS JavaScript to wolnodostêpny interpreter jêzyka JavaScript.
JavaScript jest interpretowanym jêzykiem podobnym do C, rozwijanym
przez Netscape.

Ta implementacja nie jest w 100% zgodna z jêzykiem JavaScript jaki
mo¿na znale¼æ w przegl±darkach WWW i serwerach Netscape. Aby osi±gn±æ
zamierzone cele, niezbêdne by³y pewne uproszczenia w porównaniu z
implementacj± Netscape.

%package static
Summary:	Static NGS JavaScript library
Summary(pl):	Statyczna biblioteka NGS Javascript
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description static
Static version of NGS JavaScript library.

%description static -l pl
Statyczna wersja biblioteki NGS JavaScript.

%prep
%setup -q -n js-%{version}
%patch -p1

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
install -d $RPM_BUILD_ROOT

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
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*.h
%{_infodir}/js*.info*
%{_mandir}/man1/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
