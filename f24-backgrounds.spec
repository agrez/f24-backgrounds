%global relnum 24
%global Bg_Name F%{relnum}
%global bgname %(t="%{Bg_Name}";echo ${t,,})

# Enable Extras
%global with_extras 1

Name:           %{bgname}-backgrounds
Version:        %{relnum}.1.2
Release:        1%{?dist}
Summary:        Fedora %{relnum} default desktop background

License:        CC-BY-SA
URL:            https://fedoraproject.org/wiki/F%{relnum}_Artwork
Source0:        https://fedorahosted.org/released/design-team/%{name}-%{version}.tar.xz

BuildArch:      noarch

# for %%_kde4_* macros
BuildRequires:  kde-filesystem

Requires:       %{name}-gnome = %{version}-%{release}
Requires:       %{name}-kde = %{version}-%{release}
Requires:       %{name}-xfce = %{version}-%{release}
Requires:       %{name}-mate = %{version}-%{release}


%description
This package contains desktop backgrounds for the Fedora %{relnum} default
theme.  Pulls in themes for GNOME, KDE, Mate and Xfce desktops.

%package        base
Summary:        Base images for Fedora %{relnum} default background
License:        CC-BY-SA

%description    base
This package contains base images for Fedora %{relnum} default background.


%package        kde
Summary:        Fedora %{relnum} default wallpaper for KDE

Requires:       %{name}-base = %{version}-%{release}
Requires:       kde-filesystem

%description    kde
This package contains KDE desktop wallpaper for the Fedora %{relnum}
default theme.

%package        gnome
Summary:        Fedora %{relnum} default wallpaper for Gnome and Cinnamon

Requires:       %{name}-base = %{version}-%{release}

%description    gnome
This package contains Gnome/Cinnamon desktop wallpaper for the
Fedora %{relnum} default theme.

%package        mate
Summary:        Fedora %{relnum} default wallpaper for Mate

Requires:       %{name}-base = %{version}-%{release}

%description    mate
This package contains Mate desktop wallpaper for the Fedora %{relnum}
default theme.

%package        xfce
Summary:        Fedora %{relnum} default background for XFCE4

Requires:       %{name}-base = %{version}-%{release}
Requires:       xfdesktop

%description    xfce
This package contains XFCE4 desktop background for the Fedora %{relnum}
default theme.

%if %{with_extras}
%package        extras-base
Summary:        Base images for F%{relnum} Extras Backrounds
License:        CC-BY and CC-BY-SA

%description    extras-base
This package contains base images for F%{relnum} supplemental
wallpapers.

%package        extras-gnome
Summary:        Extra F%{relnum} Wallpapers for Gnome and Cinnamon

Requires:       %{name}-extras-base

%description    extras-gnome
This package contains F%{relnum} supplemental wallpapers for Gnome
and Cinnamon

%package        extras-mate
Summary:        Extra F%{relnum} Wallpapers for Mate

Requires:       %{name}-extras-base

%description    extras-mate
This package contains F%{relnum} supplemental wallpapers for Mate

%package        extras-kde
Summary:        Extra F%{relnum} Wallpapers for KDE

Requires:       %{name}-extras-base

%description    extras-kde
This package contains F%{relnum} supplemental wallpapers for Gnome

%package        extras-xfce
Summary:        Extra F%{relnum} Wallpapers for XFCE

Requires:       %{name}-extras-base

%description    extras-xfce
This package contains F%{relnum} supplemental wallpapers for XFCE
%endif

%prep
%autosetup


%build
make %{?_smp_mflags}


%install
%make_install

%files
%doc

%files base
%license CC-BY-SA-4.0 Attribution
%dir %{_datadir}/backgrounds/%{bgname}
%dir %{_datadir}/backgrounds/%{bgname}/default
%{_datadir}/backgrounds/%{bgname}/default/normalish
%{_datadir}/backgrounds/%{bgname}/default/standard
%{_datadir}/backgrounds/%{bgname}/default/wide
%{_datadir}/backgrounds/%{bgname}/default/tv-wide
%{_datadir}/backgrounds/%{bgname}/default/%{bgname}.xml

%files kde
%{_kde4_datadir}/wallpapers/%{Bg_Name}/

%files gnome
%{_datadir}/gnome-background-properties/%{bgname}.xml

%files mate
%{_datadir}/mate-background-properties/%{bgname}.xml

%files xfce
%{_datadir}/xfce4/backdrops/%{bgname}.png

%if %{with_extras}
%files extras-base
%license CC-BY-SA-4.0 CC0-1.0 FAL-1.3 Attribution-Extras
%{_datadir}/backgrounds/%{bgname}/extras/*.jpg
%{_datadir}/backgrounds/%{bgname}/extras/*.png
%{_datadir}/backgrounds/%{bgname}/extras/%{bgname}-extras.xml

%files extras-gnome
%{_datadir}/gnome-background-properties/%{bgname}-extras.xml

%files extras-kde
%{_kde4_datadir}/wallpapers/%{Bg_Name}_*/

%files extras-mate
%{_datadir}/mate-background-properties/%{bgname}-extras.xml

%files extras-xfce
%{_datadir}/xfce4/backdrops/*.jpg
%{_datadir}/xfce4/backdrops/*.png
%endif

%changelog
* Wed May 11 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 24.1.2-1
- Upstream update fixing one wrong supplemental wallpaper 

* Wed Apr 27 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 24.1.1-1
- Upstream release of updated default wallpaper

* Sat Apr 23 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 24.1.0-1
- Added supplemental wallpapers

* Thu Feb 18 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 24.0.0-1
- Update default wallpaper
- Initial release
