#
# Conditional build:

Summary:	FREE CIVilization clone -AC version
Name:		freecivac
Version:	cvs20040405
Release:	0
License:	GPL
Group:		X11/Applications/Games/Strategy
Source0:	%{name}-%{version}.tgz
URL:		http://freecivac.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Free clone of Sid Meiers Civilization. Free Civilization clone for
unix and X. This is multiplayer strategic game and you can also play
against computer-AI players.

%prep
%setup -q -n freecivac

%build
sh autogen.sh
%configure
#%{!?with_gtk2:	--enable-client=gtk} \
#%{?with_gtk2:	--enable-client=gtk2}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
exit 1
install -d $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_datadir}/freeciv/Freeciv

install %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/freeciv/stdsounds.soundspec
cp -ar stdsounds $RPM_BUILD_ROOT%{_datadir}/freeciv

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README ChangeLog NEWS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/freeciv
%{_desktopdir}/*
%{_pixmapsdir}/*
