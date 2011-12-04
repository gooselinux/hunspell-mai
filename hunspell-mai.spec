Name: hunspell-mai
Summary: Maithili hunspell dictionaries
Version: 1.0.1
Release: 1.1%{?dist}
Group: Applications/Text
Source: http://bhashaghar.googlecode.com/files/mai_IN.oxt
URL: http://bhashaghar.googlecode.com
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2+ or LGPLv2+ or MPLv1.1
BuildArch: noarch

Requires: hunspell

%description
Maithili hunspell dictionaries.

%prep
%setup -q -c -n hunspell-mai

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p mai_IN.* $RPM_BUILD_ROOT/%{_datadir}/myspell/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_mai_IN.txt COPYING COPYING.MPL COPYING.GPL COPYING.LGPL

%{_datadir}/myspell/*

%changelog
* Tue Jan 12 2010 Parag Nemade <pnemade AT redhat.com> - 1.0.1-1.1
- Resolves: rh#543948: rebuild for rhel6.

* Mon Jan 04 2010 Parag Nemade <pnemade AT redhat.com> - 1.0.1-1
- initial version
