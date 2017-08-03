%global realname neotoma
%global upstream seancribbs
%global debug_package %{nil}


Name:		erlang-%{realname}
Version:	1.7.3
Release:	1
Summary:	Erlang library and packrat parser-generator for parsing expression grammars
Group:		Development/Erlang
License:	MIT
URL:		http://github.com/%{upstream}/%{realname}
Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
BuildRequires:	erlang-rebar


%description
Erlang library and packrat parser-generator for parsing expression grammars.


%prep
%setup -q -n %{realname}-%{version}
sed -i -e "s,git,\"%{version}\",g" src/%{realname}.app.src


%build
%{rebar_compile}


%install
mkdir -p %{buildroot}%{_erllibdir}/%{realname}-%{version}/{ebin,priv}
install -p -m 0644 ebin/%{realname}.app ebin/%{realname}*.beam %{buildroot}%{_erllibdir}/%{realname}-%{version}/ebin/
install -p -m 0644 priv/neotoma_parse.peg priv/peg_includes.hrl %{buildroot}%{_erllibdir}/%{realname}-%{version}/priv/


%check
rebar eunit -v


%files
%license LICENSE
%doc extra/ README.textile
%{_erllibdir}/%{realname}-%{version}



%changelog
* Fri May 06 2016 neoclust <neoclust> 1.7.3-2.mga6
+ Revision: 1009770
- Rebuild post boostrap
- imported package erlang-neotoma

