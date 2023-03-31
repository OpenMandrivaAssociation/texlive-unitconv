Name:		texlive-unitconv
Version:	55060
Release:	2
Summary:	Convert a length into one with another unit
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/unitconv
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unitconv.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unitconv.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package defines two macros to convert a value with unit
into one with another unit. Supported are all TeX related
units, and also km and m. The output can be in scientic
notation for large values. The package only works with
LuaLaTeX!

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/lualatex/unitconv
%doc %{_texmfdistdir}/doc/lualatex/unitconv

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
