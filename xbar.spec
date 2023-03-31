Name:           xbar
Version:        0.0.1
Release:        2
Summary:        Tiny XCB information bar
License:        MIT
URL:            https://github.com/mcpcpc/xbar
Source0:        https://github.com/mcpcpc/xbar/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-keysyms)

%description
xbar is a tiny XCB status bar. An incredibly lightweight information bar,
designed to print important real-time system metrics. Beyond foreground and
background colors, xbar offers limited customization for a distraction-free
user experience.

%prep
%autosetup

%build
%make_build \
  CFLAGS="%{optflags}" \
  LDFLAGS="%{build_ldflags}"

%install
%make_install PREFIX="%{_prefix}"

%files
%license LICENSE
%doc README CHANGELOG
%{_bindir}/xbar
